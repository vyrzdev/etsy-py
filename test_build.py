from src import client, rq

with open("token.txt", "r") as token_file:
    requester = rq.EtsyRequester(auth_mode="api_key", api_key=token_file.readlines()[0][:-1])


etsyClient = client.EtsyClient(requester)
print(etsyClient.getListing(listing_id="734131682").response.content)


