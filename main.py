# Read the value of array : unmanaged and for every element use the logic : take id and type and generate terraform import command:
# Input: JSON(results.json)
# Output: terraform import resource_name.module_name id

import json
def generate_terraform_import_commands(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        if "unmanaged" in data:
            unmanaged_resources = data["unmanaged"]
            for idx, resource in enumerate(unmanaged_resources, start=1):
                resource_id = resource.get("id")
                resource_type = resource.get("type")
                if resource_id and resource_type:
                    # Split the resource_type to get the provider and resource name
                    provider, _, resource_name = resource_type.partition("_")
                    module_name = f"resource {idx}"
                    import_command = f"terraform import {provider}.{resource_name}.{module_name} {resource_id}"
                    print(import_command)
                else:
                    print(f"Skipping invalid resource: {resource}")

    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

# Example usage:
json_file_path = "result.json"
generate_terraform_import_commands(json_file_path)


# to run: /opt/homebrew/bin/python3 /Users/divyashukla/Desktop/GenAI/main.py
