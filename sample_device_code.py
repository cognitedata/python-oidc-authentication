from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import Token
from msal import PublicClientApplication

# Contact Project Administrator to get these
TENANT_ID = "<Tenant ID>"
CLIENT_ID = "<Client ID>"
CDF_CLUSTER = "<cluster>"  # api, westeurope-1 etc
COGNITE_PROJECT = "<cdf project>"

BASE_URL = f"https://{CDF_CLUSTER}.cognitedata.com"
SCOPES = [f"https://{CDF_CLUSTER}.cognitedata.com/.default"]

AUTHORITY_HOST_URI = "https://login.microsoftonline.com"
AUTHORITY_URI = AUTHORITY_HOST_URI + "/" + TENANT_ID


def authenticate_device_code():

    app = PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY_URI)

    device_flow = app.initiate_device_flow(scopes=SCOPES)
    print(device_flow["message"])  # print device code to screen
    creds = app.acquire_token_by_device_flow(flow=device_flow)

    return creds


creds = authenticate_device_code()

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

cnf = ClientConfig(client_name="my-special-client", project=COGNITE_PROJECT, credentials=Token(creds["access_token"]), base_url=BASE_URL)
client = CogniteClient(cnf)

print(client.iam.token.inspect())
