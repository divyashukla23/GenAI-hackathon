# # Read the value of array : unmanaged and for every element use the logic : take id and type and generate terraform import command:
# # Input: JSON(results.json)
# # Output: terraform import resource_name.module_name id
import json
def generate_terraform_import_commands(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        if "unmanaged" in data:
            unmanaged_resources = data["unmanaged"]
            commands = []  # To store the Terraform import commands

            for idx, resource in enumerate(unmanaged_resources, start=1):
                resource_id = resource.get("id")
                resource_type = resource.get("type")
                if resource_id and resource_type:
                    module_name = f"resource{idx}"
                    import_command = f"terraform import {resource_type}.{module_name} {resource_id}"
                    tf_block = f"resource \"{resource_type}\" \"{module_name}\"{{}}"
                    commands.append(import_command)
                    commands.append(tf_block)
                else:
                    print(f"Skipping invalid resource: {resource}")

            # Save the Terraform import commands to a bash script file
            with open("command.sh", "w") as bash_file:
                for command in commands:
                    bash_file.write(command + "\n")
            # Print the commands to the console (optional)
            # for command in commands:
            #     print(command)

    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

# Example usage:
json_file_path = "result.json"
generate_terraform_import_commands(json_file_path)
