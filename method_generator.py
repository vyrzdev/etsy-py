import re
import json

with open("current_method_table.json", "r") as method_table_file:
    method_table_json_str = method_table_file.read()
    methods_table = json.loads(method_table_json_str)

print(f"Found {methods_table.get('count')} methods in current_method_table.json")

methods_file = open("src/methods.py", "r")
print(methods_table)

currently_implemented_methods = dict()

capture = False
for line in methods_file.readlines():
    if "# StartMethod:" in line:
        capture = True
        method_name = re.search(": ?(\w+)", line).group(1)
        method_code = ""
    elif "# EndMethod:" in line:
        capture = False
        ended_method = re.search(": ?(\w+)", line).group(1)
        if ended_method != method_name:
            print(f"UNFINISHED METHOD: {method_name}")
            exit()
        else:
            currently_implemented_methods.update(**{method_name: method_code})
            ended_method = None
            method_name = None
    else:
        if capture:
            method_code += line
        else:
            pass
if capture:
    print(f"UNFINISHED METHOD: {method_name}")
    exit()


def generate_method_code(method_definition_json: dict) -> list:
    params: dict = method_definition_json.get("params")
    if params is None:
        params = {}
    uri = method_definition_json["uri"]
    uri_params = re.findall(':(\w+)(?:\/|$)', uri)
    definition_line = f"def {method_definition_json['name']}(self,"
    args = ""
    for param in uri_params:
        try:
            args += f" {param},"
        except KeyError:
            print(f"Incorrectly written method_definition for method: {method_definition_json['name']}\n"
                  f"Missing a required parameter: {param}\n"
                  f"Ignoring for now...",
                  )
            args += f" {param},"
    if method_definition_json["http_method"] in ["POST", "PUT"]:
        args += " data=None,"
    args += " query_params=None"
    definition_line += args
    definition_line += "):"

    if method_definition_json["visibility"] == "private":
        oauth_check_lines = [
            f"    if self.requester.auth_mode == 'api_key':",
            f"        raise RequiresOauth"
        ]
    else:
        oauth_check_lines = []

    uri_param_string = "["
    for uri_param in uri_params:
        uri_param_string += f" {uri_param},"
    uri_param_string += "]"
    request_line = f"    return self.requester.make_request(uri='{method_definition_json['uri']}', uri_params={uri_param_string}, method='{method_definition_json['http_method']}', query_params=query_params,"
    if method_definition_json["http_method"] in ["POST", "PUT"]:
        request_line += " data=data,"
    request_line += ")"

    code = [
        definition_line,
        *oauth_check_lines,
        request_line
    ]
    return code



method_definitions = {}
for method in methods_table.get("results"):
    code = "\n".join(generate_method_code(method))
    method_definitions.update(**{method["name"]: code})

with open("src/methods.py", "w") as build_file:
    file_header_lines = [
        "from .rq import RequiresOauth\n",
        "\n# These methods are all auto-generated from the Etsy Method Table, by method_generator.py periodically",
        "# Any manual changes will be overwritten!\n"
    ]
    header = "\n".join(file_header_lines)

    methods_raw = ""
    for method, code in method_definitions.items():
        method_raw = f"\n# StartMethod: {method}\n{code}\n# EndMethod: {method}\n\n"
        methods_raw += method_raw

    build = f"{header}\n{methods_raw}"

    build_file.write(build)


def generate_stub_definition(method_definition_json):
    params: dict = method_definition_json["params"]
    if params is None:
        params = {}
    uri = method_definition_json["uri"]
    uri_params = re.findall(':(\w+)(?:\/|$)', uri)
    definition_line = f"    def {method_definition_json['name']}(self,"
    args = ""
    for param in uri_params:
        try:
            args += f" {param},"
        except KeyError:
            print(f"Incorrectly written method_definition for method: {method_definition_json['name']}\n"
                  f"Missing a required parameter: {param}\n"
                  f"Ignoring for now...",
                  )
            args += f" {param},"
    if method_definition_json["http_method"] in ["POST", "PUT"]:
        args += " data: typing.Union[None, dict] = ...,"
    args += " query_params: typing.Union[None, dict] = ..."
    definition_line += args
    definition_line += ") -> rq.EtsyResponse: ..."
    return "\n".join([
        definition_line
    ])


stub_file_code = ""
for method in methods_table["results"]:
    stub_file_code += f"\n{generate_stub_definition(method)}\n"

with open("src/base_client.pyi", "r") as base_client_stub:
    with open("src/client.pyi", "w") as build_file:
        raw = f"{base_client_stub.read()}\n    # Autogenerated Stubs...\n{stub_file_code}"
        build_file.write(raw)


