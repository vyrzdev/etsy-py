import jinja2
import dataclasses
import typing
import json
import re


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('auto_generation/templates'),
)


@dataclasses.dataclass
class Method:
    name: str
    uri: str
    oauth_required: bool
    uri_parameters: typing.List[str]
    http_method: str


with open("current_method_table.json", "r") as current_method_table_file:
    method_table = json.loads(current_method_table_file.read())


with open("current_release.json", "r") as current_release_json_file:
    current_release = json.loads(current_release_json_file.read())

print(current_release["api_version"])
current_release["api_version"] += 1
print(current_release["api_version"])

with open("current_release.json", "w") as current_release_json_file:
    current_release_json_file.write(json.dumps(current_release))


built_methods: typing.List[Method] = list()
for method_json in method_table.get("results"):
    uri_parameters = re.findall(':(\w+)(?:\/|$)', method_json.get("uri"))
    print(uri_parameters)

    built_methods.append(Method(
        name=method_json.get("name"),
        uri=method_json.get("uri"),
        oauth_required=(method_json.get("visibility") == "private"),
        uri_parameters=uri_parameters,
        http_method=method_json.get("http_method")
    ))

new_methods_py_str = env.get_template("methods_py_template.jinja2").render(methods=built_methods)
with open("etsy_py/methods.py", "w") as new_methods_py_file:
    new_methods_py_file.write(new_methods_py_str)

new_client_pyi_str = env.get_template("client_pyi_template.jinja2").render(methods=built_methods)
with open("etsy_py/client.pyi", "w") as new_client_pyi_file:
    new_client_pyi_file.write(new_client_pyi_str)

print(f"ON THE EXIT OF GENERATOR::: API_VERSION={current_release['api_version']}")


