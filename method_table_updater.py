import requests
import json


with open("token.txt", "r") as token_file:
    methods_table = requests.get("https://openapi.etsy.com/v2/", params={"api_key": token_file.read()[:-1]}).json()


with open("current_method_table.json", "r+") as current_method_table_json_file:
    existing_table = json.loads(current_method_table_json_file.read())
    if existing_table != methods_table:
        print("Updating current_method_table.json")
        current_method_table_json_file.seek(0)
        current_method_table_json_file.write(json.dumps(methods_table))
        current_method_table_json_file.truncate()
    else:
        print("Current table up to date! No changes applied!")



