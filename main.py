# # Read the value of array : unmanaged and for every element use the logic : take id and type and generate terraform import command:
# # Input: JSON(results.json)
# # Output: terraform import resource_name.module_name id
import json
import subprocess
import os
import openai
import re

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
                bash_file.write("terraform init" + "\n")
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

def import_terraform_state():
    # Path to the shell script
    script_path = "./command.sh"

    os.chmod(script_path, os.stat(script_path).st_mode | 0o111)
    # Execute the shell script
    result = subprocess.run([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if the script ran successfully
    if result.returncode == 0:
        print('Shell script ran successfully.')
        print('Output:', result.stdout.decode())
    else:
        print('Shell script failed.')
        print('Error:', result.stderr.decode())

def cleanup_files():
    files_to_delete = ['command.sh', 'main.tf']

    for file in files_to_delete:
        try:
            os.remove(file)
            print(f'{file} has been deleted successfully.')
        except FileNotFoundError:
            print(f'{file} does not exist.')
        except PermissionError:
            print(f'Permission denied when trying to delete {file}.')
        except Exception as e:
            print(f'An error occurred while trying to delete {file}: {e}')

json_file_path = "result.json"
generate_terraform_import_commands(json_file_path)
import_terraform_state()

# Read the contents of the main prompt file
with open("prompt.txt", "r") as file:
    prompt_lines = file.readlines()

# File paths and their respective insertion line numbers
files_info = {
    "infrastructure/main.tf": 160,
    "infrastructure/providers.tf": 165,
    "infrastructure/variables.tf": 170,
    "infrastructure/terraform.tfvars": 175,
    "infrastructure/outputs.tf": 180,
    "terraform.tfstate": 151
}

# Sorting the file paths based on their insertion line numbers in descending order
sorted_files_info = sorted(files_info.items(), key=lambda x: x[1], reverse=True)

# Insert the contents of each file at the specified line number in descending order
for file_path, line_num in sorted_files_info:
    with open(file_path, "r") as file:
        content = file.readlines()
    # Adjusting for 0-indexing in Python lists
    prompt_lines[line_num-1:line_num-1] = content

prompt = ''.join(prompt_lines)

# Load your API key from an environment variable or secret management service

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

data = json.loads(chat_completion.choices[0].message["content"])

# Create 'output' directory if it doesn't exist
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Write the contents of each file from the JSON to actual files in 'output' directory
for filename, content in data.items():
    with open(os.path.join(output_dir, filename), 'w') as file:
        file.write(content)

cleanup_files()