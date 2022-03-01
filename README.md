# OIDC authentication with Cognite Python SDK

The python SDK can be authenticated using:
* a token retrieved when a user authenticates (running as personal user). 
* a static client secret, for long running jobs / extractors

A requirement is to set up your project with OIDC.

# Personal authentication with interactive login
You can get a token by doing an interactive login a the browser. This is the preferred approach for users to access CDF when running scripts or using Jupyter. If a browser is not available you can use the "device code flow" described below.

See the sample in [sample_interactive_login.py](sample_interactive_login.py). Update variables `CLIENT_ID`, `TENANT_ID`, `CDF_CLUSTER` and `COGNITE_PROJECT` to match your setup.

# Authentication with personal credentials using device code

If a browser is not available, e.g. if you are logged into a terminal, the “code flow grant” needs to be followed. To use this flow the App Registration needs to be setup with “Allow public client flows” under Authentication.

See the sample in [sample_device_code.py](sample_device_code.py). Update variables `CLIENT_ID`, `TENANT_ID`, `CDF_CLUSTER` and `COGNITE_PROJECT` to match your setup.

# Personal authentication with interactive login with token refresh

The token retrieved in the two samples above will expire in 1 hour, and you will have to run the code again. To avoid that the MSAL implements support for using a refresh token to re-authenticate without user interaction.
The code is very similar, but we need make sure to reuse the `PublicClientApplication` is reused, and then we give a `Callable` to the `CogniteClient` which will make the SDK ask for a new token on each request. The token will be served from a memory cache, but refreshed if needed (no user login or device code is needed for refresh).

See the sample in [sample_interactive_login_token_refresh.py](sample_interactive_login_token_refresh.py). Update variables `CLIENT_ID`, `TENANT_ID`, `CDF_CLUSTER` and `COGNITE_PROJECT` to match your setup.

# Authentication with client secret

The SDK supports using client secrets directly by providing the client directly to the CogniteClient with the `token_client_secret`, `token_client_id`, `token_url` and  `token_scopes`. This should be used for long running jobs like an extractor.

See the sample in [sample_client_secret.py](sample_client_secret.py). Update variables `CLIENT_ID`, `TENANT_ID`, `CDF_CLUSTER` and `COGNITE_PROJECT` to match your setup.

Make sure the `COGNITE_API_KEY` environment variable are not set, it will override the token setup.
 
