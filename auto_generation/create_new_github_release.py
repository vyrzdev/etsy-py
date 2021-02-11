import github
import sys
import json
import os


with open("current_release.json", "r") as current_release_json_file:
    current_release_json = json.loads(current_release_json_file.read())


latest_commit_hash = os.popen("git rev-parse HEAD").readlines()[0].strip("\n")

version_tag = f"etsy-py-feature-v{current_release_json.get('feature_version')}-api-v{current_release_json.get('api_version')}"

github_token = str(sys.argv[1])
client = github.Github(github_token)

repository = client.get_repo("vyrzdev/etsy-py")
repository.create_git_tag_and_release(
    tag=version_tag,
    tag_message=f"Release for Feature Version: {current_release_json.get('feature_version')} and API Version: {current_release_json.get('api_version')}",
    release_name=version_tag,
    release_message=f"Release for Feature Version: {current_release_json.get('feature_version')} and API Version: {current_release_json.get('api_version')}",
    object=latest_commit_hash,
    type="commit"
)

