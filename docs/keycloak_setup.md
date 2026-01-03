# Keycloak Setup for Auth Demo

This guide explains how to use Keycloak with the `08_auth_time_http.py` server for authentication demonstrations.

## Overview

The workshop includes a Docker Compose setup to run Keycloak locally. This allows you to demonstrate:
- OAuth2/OIDC authentication flows
- JWT token validation with RS256 (public key cryptography)
- Integration with an external Identity Provider (IdP)

## Quick Start

### 1. Start Keycloak

```bash
cd docker
docker compose -f compose.keycloak.yml up -d
```

Keycloak will be available at: http://localhost:8080

Default admin credentials:
- Username: `admin`
- Password: `admin`

### 2. Access Keycloak Admin Console

Visit http://localhost:8080 and log in with the admin credentials.

### 3. Realm Configuration (TODO)

The current `realm.json` is a placeholder. To set up a proper realm:

1. Create a new realm called `mcp-workshop`
2. Create a client for the workshop:
   - Client ID: `mcp-workshop-client`
   - Client Protocol: `openid-connect`
   - Access Type: `confidential` or `public` (depending on your demo needs)
   - Valid Redirect URIs: `http://localhost:8000/*`
3. Create test users (e.g., `alice`, `bob`)
4. Export the realm configuration and replace `docker/realm.json`

### 4. Integrate with Server 08

Currently, `servers/08_auth_time_http.py` uses a simple HS256 JWT for development (secret: `dev-secret-change-me`).

To integrate with Keycloak:

1. Update the server to fetch Keycloak's JWKS endpoint
2. Validate RS256 tokens instead of HS256
3. Extract user claims from the Keycloak-issued JWT

Example code changes needed in `08_auth_time_http.py`:

```python
# Fetch JWKS from Keycloak
KEYCLOAK_URL = "http://localhost:8080"
REALM = "mcp-workshop"
JWKS_URL = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/certs"

# Validate RS256 token
import jwt
from jwt import PyJWKClient

jwks_client = PyJWKClient(JWKS_URL)
signing_key = jwks_client.get_signing_key_from_jwt(token)
claims = jwt.decode(
    token,
    signing_key.key,
    algorithms=["RS256"],
    audience="mcp-workshop-client",
)
```

### 5. Get a Token from Keycloak

For demos, you can use the Direct Access Grant (Resource Owner Password Credentials) flow:

```bash
curl -X POST "http://localhost:8080/realms/mcp-workshop/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=mcp-workshop-client" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "username=alice" \
  -d "password=alice123" \
  -d "grant_type=password"
```

> **Security Note**: In production, never hardcode client secrets. Use environment variables or a secure secret management system (e.g., HashiCorp Vault, AWS Secrets Manager). Store the client secret in an `.env` file (already in `.gitignore`) and load it securely.

The response will include an `access_token` you can use with the `/time` endpoint.

### 6. Test the Authenticated Endpoint

```bash
TOKEN="eyJhbGc..."  # Your Keycloak token
curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:8000/time
```

## Development vs Production

**Development Mode (Current)**:
- Uses HS256 with a shared secret
- Simple, fast, no external dependencies
- Good for initial demos and testing
- Token generation: `./scripts/get_token.sh alice`

**Production-Like Mode (With Keycloak)**:
- Uses RS256 with public key validation
- Centralized identity management
- Demonstrates real-world auth patterns
- Requires Keycloak running

## Security Notes

- The current `dev-secret-change-me` is intentionally insecure for demos
- Never use HS256 with weak secrets in production
- Keycloak tokens should be validated against the IdP's public keys (JWKS)
- Always use HTTPS in production
- Rotate secrets and tokens regularly

## Troubleshooting

### Keycloak won't start

Ensure port 8080 is available:
```bash
lsof -i :8080
```

### Realm import fails

Check the `realm.json` syntax. It should be a valid Keycloak realm export.

### Token validation fails

- Verify the token hasn't expired
- Check the `audience` (aud) claim matches your client ID
- Ensure the signing algorithm matches (HS256 vs RS256)

## References

- [Keycloak Documentation](https://www.keycloak.org/documentation)
- [JWT.io](https://jwt.io) - for debugging tokens
- [OAuth 2.0 RFC](https://tools.ietf.org/html/rfc6749)
