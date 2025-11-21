import argparse
import pprint

from .client import MolgenisAuthClient


def main():
    parser = argparse.ArgumentParser(
        description="Authenticate with Molgenis using OAuth Device Flow"
    )
    parser.add_argument(
        "--auth-server",
        required=True,
        help="Base URL of the Molgenis authentication server",
    )
    parser.add_argument(
        "--client-id",
        required=True,
        help="OAuth client ID",
    )
    parser.add_argument(
        "--scopes",
        default="openid offline_access",
        help="OAuth scopes (default: openid offline_access)",
    )

    args = parser.parse_args()

    client = MolgenisAuthClient(
        auth_server=args.auth_server,
        client_id=args.client_id,
        scopes=args.scopes,
    )

    token = client.device_flow_auth()
    print("\n=== Authentication Successful ===")
    pprint.pprint(token)
