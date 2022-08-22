from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials
import os

# Contact Project Administrator to get these
TENANT_ID = "<Tenant ID>"
CLIENT_ID = "<Client ID>"
CDF_CLUSTER = "<cluster>"  # api, westeurope-1 etc
COGNITE_PROJECT = "<cdf project>"

SCOPES = [f"https://{CDF_CLUSTER}.cognitedata.com/.default"]

CLIENT_SECRET = os.getenv("CLIENT_SECRET")  # store secret in env variable

TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

creds=OAuthClientCredentials(token_url=TOKEN_URL, client_id= CLIENT_ID, scopes= SCOPES, client_secret= CLIENT_SECRET)

cnf = ClientConfig(client_name="my-special-client", project=COGNITE_PROJECT, credentials=creds, base_url=f"https://{CDF_CLUSTER}.cognitedata.com")

client = CogniteClient(cnf)

print(client.iam.token.inspect())
