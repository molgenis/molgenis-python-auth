# molgenis-python-auth

A lightweight Python client for performing **OAuth 2.0 Device Authorization Flow**
with the **Molgenis Authentication Server**.

## Installation

```bash
pip install git+https://github.com/molgenis/molgenis-python-auth.git
```

## Quick start

```python
from molgenis_auth import MolgenisAuthClient

client = MolgenisAuthClient(
    auth_server="https://auth.molgenis.org",
    client_id="YOUR_CLIENT_ID",
    scopes="openid offline_access",
)

tokens = client.device_flow_auth()
```

## CLI usage

```bash
molgenis-auth \
    --auth-server https://auth.molgenis.org \
    --client-id YOUR_CLIENT_ID \
    --scopes "openid offline_access"
```
