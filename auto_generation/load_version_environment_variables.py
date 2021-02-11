import os
import json


with open("current_release.json", "r") as current_release_json_file:
    current_release_json = json.loads(current_release_json_file.read())
    os.putenv("CURRENT_FEATURE_VERSION", str(current_release_json.get("feature_version")))
    os.putenv("CURRENT_API_VERSION", str(current_release_json.get("api_version")))

