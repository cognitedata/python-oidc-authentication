from cognite.client import CogniteClient
from msal import PublicClientApplication

# Contact Project Administrator to get these
TENANT_ID = "<Tenant ID>"
CLIENT_ID = "<Client ID>"
CDF_CLUSTER = "<cluster>"  # api, westeurope-1 etc
COGNITE_PROJECT = "<cdf project>"

SCOPES = [f"https://{CDF_CLUSTER}.cognitedata.com/.default"]

AUTHORITY_HOST_URI = "https://login.microsoftonline.com"
AUTHORITY_URI = AUTHORITY_HOST_URI + "/" + TENANT_ID

app = PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY_URI)


def authenticate_device_code(app):
    # Firstly, check the cache to see if this end user has signed in before
    accounts = app.get_accounts()
    if accounts:
        creds = app.acquire_token_silent(SCOPES, account=accounts[0])
    else:
        device_flow = app.initiate_device_flow(scopes=SCOPES)
        print(device_flow["message"])  # print device code to screen
        creds = app.acquire_token_by_device_flow(flow=device_flow)
    return creds


def get_token():
    return authenticate_device_code(app)["access_token"]


client = CogniteClient(
    token_url=f"{AUTHORITY_URI}/v2.0",
    token=get_token,
    token_client_id=CLIENT_ID,
    project=COGNITE_PROJECT,
    base_url=f"https://{CDF_CLUSTER}.cognitedata.com",
    client_name="cognite-python-dev",
)
print(client.iam.token.inspect())
