from src import oauth_helper, client, rq

with open("token.txt", "r") as token_file:
    helper = oauth_helper.EtsyOauthHelper(token_file.read()[:-1], shared_secret="$Removed_Secret")

login_url, temp_oauth_token, temp_oauth_secret = helper.get_login_url(permission_scopes=["listings_r"])

print(login_url)

verifier = input("- ")

oauth_credentials = helper.get_permanent_credentials(temp_oauth_token, temp_oauth_secret, verifier)

etsy_requester = rq.EtsyRequester(
    auth_mode="oauth",
    oauth_credentials=oauth_credentials
)

etsy_client = client.EtsyClient(
    requester=etsy_requester,
)

print(etsy_client.getMethodTable().response.content)
print(etsy_client.findAllShopListingsInactive("23471684").response.content)