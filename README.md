# Molgenis Python Auth Client
A lightweight Python client for performing **OAuth 2.0 Device Authorization Flow** with the **Molgenis Authentication Server**.
This package allows you to authenticate users either:

* ✔ From the **command line** (CLI), or
* ✔ Programmatically in **your own Python project**

It opens the user's browser, waits for authorization, and returns the OAuth token payload when authentication is complete.

## ✨ Features
* 🔐 Implements OAuth 2.0 Device Flow
* 🌐 Automatic OpenID Connect discovery
* 🧭 Simple command-line interface (`molgenis-auth`)
* 🐍 Clean Python API for integration in your application
* 🕒 Handles `authorization_pending`, `slow_down`, and timeout conditions

## 📦 Installation
Install from source / local checkout
```commandline
git clone https://github.com/YOURNAME/MolgenisPythonAuth.git
cd MolgenisPythonAuth
pip install -e .
```
The `-e` flag installs in editable mode for development.

## 🖥️ Command-Line Usage

After installation, the CLI tool `molgenis-auth` becomes available.

Authenticate using the Molgenis Auth Server
```commandline
molgenis-auth \
    --auth-server https://auth.molgenis.org \
    --client-id YOUR_CLIENT_ID \
    --scopes "openid offline_access"
```

### What the CLI does
1. Discovers OpenID configuration
2. Requests a device authorization code
3. Opens your browser
4. Waits until you authenticate
5. Prints the OAuth token response JSON

Example output:
```json
{
    "access_token": "eyJhbGciOiJIUz...",
    "expires_in": 3600,
    "refresh_token": "def50200a4...",
    "scope": "openid offline_access",
    "token_type": "Bearer"
}
```

## 🐍 Python API Usage

Import the client and call `device_flow_auth()`:

```python
from molgenis_auth import MolgenisAuthClient

client = MolgenisAuthClient(
    auth_server="https://auth.molgenis.org",
    client_id="YOUR_CLIENT_ID",
    scopes="openid offline_access",
)

tokens = client.device_flow_auth()
print(tokens)
```

### What the Python API does
1. Performs discovery via `.well-known/openid-configuration`
2. Requests the device code
3. Opens a browser window for login
4. Polls until authorization or timeout
5. Returns the final OAuth token JSON

All error conditions (timeouts, unsupported operations, invalid credentials) raise informative Python exceptions.

## 📁 Project Structure
```commandline
molgenis_auth/
    cli.py
    client.py
    __init__.py
setup.py
README.md
```

## 🛠 Development Setup

Create a virtual environment:
```commandline
python3 -m venv venv
source venv/bin/activate
pip install -e .
```
Run the CLI:

```commandline
molgenis-auth --help
```

## 📄 License

GNU General Public License — Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

## 🤝 Contributing

Pull requests are welcome!
If you have feature ideas (saving tokens locally, adding a refresh endpoint, integrating with Molgenis APIs), open an issue.

## 💬 Support

If you have questions or run into issues, please open a GitHub issue in the repository.