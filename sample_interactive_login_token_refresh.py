import atexit
import os

from cognite.client import CogniteClient
from msal import PublicClientApplication, SerializableTokenCache

# Contact Project Administrator to get these
TENANT_ID = "<Tenant ID>"
CLIENT_ID = "<Client ID>"
CDF_CLUSTER = "<cluster>"  # api, westeurope-1 etc
COGNITE_PROJECT = "<cdf project>"

CACHE_FILENAME = "cache.bin"
SCOPES = [f"https://{CDF_CLUSTER}.cognitedata.com/.default"]

AUTHORITY_HOST_URI = "https://login.microsoftonline.com"
AUTHORITY_URI = AUTHORITY_HOST_URI + "/" + TENANT_ID
PORT = 53000


def create_cache():
    cache = SerializableTokenCache()
    if os.path.exists(CACHE_FILENAME):
        cache.deserialize(open(CACHE_FILENAME, "r").read())
    atexit.register(lambda:
        open(CACHE_FILENAME, "w").write(cache.serialize()) if cache.has_state_changed else None
    )
    return cache


def authenticate_azure(app):
    # Firstly, check the cache to see if this end user has signed in before
    accounts = app.get_accounts()
    if accounts:
        creds = app.acquire_token_silent(SCOPES, account=accounts[0])
    else:
        # interactive login - make sure you have http://localhost:port in Redirect URI in App Registration as type "Mobile and desktop applications"
        creds = app.acquire_token_interactive(scopes=SCOPES, port=PORT,)

    return creds


app = PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY_URI, token_cache=create_cache())


def get_token():
    return authenticate_azure(app)["access_token"]


client = CogniteClient(
    token_url=f"{AUTHORITY_URI}/v2.0",
    token=get_token,
    token_client_id=CLIENT_ID,
    project=COGNITE_PROJECT,
    base_url=f"https://{CDF_CLUSTER}.cognitedata.com",
    client_name="cognite-python-dev",
    debug=True,
)

print(client.iam.token.inspect())
