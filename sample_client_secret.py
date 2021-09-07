from cognite.client import CogniteClient
import os

# Contact Project Administrator to get these
TENANT_ID = "<Tenant ID>"
CLIENT_ID = "<Client ID>"
CDF_CLUSTER = "<cluster>"  # api, westeurope-1 etc
COGNITE_PROJECT = "<cdf project>"

SCOPES = [f"https://{CDF_CLUSTER}.cognitedata.com/.default"]

CLIENT_SECRET = os.getenv("CLIENT_SECRET")  # store secret in env variable

TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

client = CogniteClient(
    token_url=TOKEN_URL,
    token_client_id=CLIENT_ID,
    token_client_secret=CLIENT_SECRET,
    token_scopes=SCOPES,
    project=COGNITE_PROJECT,
    base_url=f"https://{CDF_CLUSTER}.cognitedata.com",
    client_name="client_secret_test_script",
    debug=True,
)

print(client.iam.token.inspect())
