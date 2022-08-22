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


def authenticate_device_code():

    app = PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY_URI)

    device_flow = app.initiate_device_flow(scopes=SCOPES)
    print(device_flow["message"])  # print device code to screen
    creds = app.acquire_token_by_device_flow(flow=device_flow)

    return creds


creds = authenticate_device_code()

cnf = ClientConfig(client_name="my-special-client", project=COGNITE_PROJECT, credentials=Token(creds["access_token"]), base_url=f"https://{CDF_CLUSTER}.cognitedata.com")
client = CogniteClient(cnf)

print(client.iam.token.inspect())
