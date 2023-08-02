# # Read the value of array : unmanaged and for every element use the logic : take id and type and generate terraform import command:
# # Input: JSON(results.json)
# # Output: terraform import resource_name.module_name id
import json
import subprocess

def generate_terraform_import_commands(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        if "unmanaged" in data:
            unmanaged_resources = data["unmanaged"]
            terraform_import_commands = []
            terraform_resource_blocks = []

            for idx, resource in enumerate(unmanaged_resources, start=1):
                resource_id = resource.get("id")
                resource_type = resource.get("type")
                if resource_id and resource_type:
                    module_name = f"resource{idx}"
                    terraform_import_command = f"terraform import {resource_type}.{module_name} {resource_id}"
                    terraform_resource_block = f"resource \"{resource_type}\" \"{module_name}\"{{}}"
                    terraform_import_commands.append(terraform_import_command)
                    terraform_resource_blocks.append(terraform_resource_block)
                else:
                    print(f"Skipping invalid resource: {resource}")

            # Save the Terraform import commands to a bash script file
            with open("command.sh", "w") as bash_file:
                bash_file.write("#!/bin/bash" + "\n")
                for terraform_import_command in terraform_import_commands:
                    bash_file.write(terraform_import_command + "\n")

            # Save terraform resource blocks
            with open("main.tf", "w") as terraform_resource_file:
                for terraform_resource_block in terraform_resource_blocks:
                    terraform_resource_file.write(terraform_resource_block + "\n")

    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

# Example usage:
json_file_path = "result.json"
generate_terraform_import_commands(json_file_path)

# Path to the shell script
script_path = "./command.sh"

# Execute the shell script
result = subprocess.run([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Check if the script ran successfully
if result.returncode == 0:
    print('Shell script ran successfully.')
    print('Output:', result.stdout.decode())
else:
    print('Shell script failed.')
    print('Error:', result.stderr.decode())