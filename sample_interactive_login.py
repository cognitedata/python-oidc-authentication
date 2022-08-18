from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import Token
from msal import PublicClientApplication

# Contact Project Administrator to get these
TENANT_ID = "<Tenant ID>"
CLIENT_ID = "<Client ID>"
CDF_CLUSTER = "<cluster>"  # api, westeurope-1 etc
COGNITE_PROJECT = "<cdf project>"

SCOPES = [f"https://{CDF_CLUSTER}.cognitedata.com/.default"]

AUTHORITY_HOST_URI = "https://login.microsoftonline.com"
AUTHORITY_URI = AUTHORITY_HOST_URI + "/" + TENANT_ID
PORT = 53000


def authenticate_azure():

    app = PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY_URI)

    # interactive login - make sure you have http://localhost:port in Redirect URI in App Registration as type "Mobile and desktop applications"
    creds = app.acquire_token_interactive(scopes=SCOPES, port=PORT)
    return creds


creds = authenticate_azure()

cnf = ClientConfig(client_name="my-special-client", project="my-project", credentials=Token(creds["access_token"]))
client = CogniteClient(cnf)


print(client.iam.token.inspect())
