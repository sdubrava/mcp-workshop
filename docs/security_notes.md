# Security Notes

This workshop includes an intentionally vulnerable server (`06_security_vuln_stdio.py`).

## Threat model basics

- Treat tool calls as **untrusted input**.
- Assume an attacker can influence tool parameters.

## Workshop examples

### Vulnerable pattern

- `shell=True`
- passing user input directly to a shell

### Hardened pattern

- strict allowlists
- no shell
- tight timeouts
- output truncation
- minimal filesystem/network access

## TODO hardening ideas

- run servers in containers with seccomp/apparmor
- drop privileges
- add authentication/authorization (see server 08 + Keycloak materials)
- add audit logging and rate limiting
