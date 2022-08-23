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

BASE_URL = f"https://{CDF_CLUSTER}.cognitedata.com"

creds=OAuthClientCredentials(token_url=TOKEN_URL, client_id= CLIENT_ID, scopes= SCOPES, client_secret= CLIENT_SECRET)

# Configuration object for the client
#     Args:
#         client_name (str): A user-defined name for the client. Used to identify number of unique applications/scripts
#             running on top of CDF.
#         project (str): Project. Defaults to project of given API key.
#         credentials (CredentialProvider): Credentials. e.g. APIKey, Token, ClientCredentials.
#         api_subversion (str): API subversion
#         base_url (str): Base url to send requests to. Defaults to "https://api.cognitedata.com"
#         max_workers (int): Max number of workers to spawn when parallelizing data fetching. Defaults to 10.
#         headers (Dict): Additional headers to add to all requests.
#         timeout (int): Timeout on requests sent to the api. Defaults to 30 seconds.
#         file_transfer_timeout (int): Timeout on file upload/download requests. Defaults to 600 seconds.
#         debug (bool): Configures logger to log extra request details to stderr.

cnf = ClientConfig(client_name="my-special-client", project=COGNITE_PROJECT, credentials=creds, base_url=BASE_URL)

client = CogniteClient(cnf)

print(client.iam.token.inspect())
