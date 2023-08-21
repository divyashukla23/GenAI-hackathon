import subprocess

def main():
    # Execute the command to get the list of resources
    resources = run_command("terraform state list").splitlines()

    for resource in resources:
        # Prompt user for input
        user_input = input(f"Enter input for the resource {resource}: ")
        resource_type = resource.split(".")[0]

        # Construct the command
        command = f"terraform state mv -state=terraform.tfstate -state-out=infrastructure/terraform.tfstate {resource} {resource_type}.{user_input}"

        # Execute the command
        try:
            run_command(command)
            print(f"Moved {resource} successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error moving {resource}: {e}")

def run_command(command):
    """Execute a shell command and return its output."""
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
    return result.stdout.decode()

def replace_file_content(source_file_path, target_file_path):
    """Replace the content of target_file_path with the content of source_file_path."""
    with open(source_file_path, 'r') as source_file:
        content = source_file.read()
    
    with open(target_file_path, 'w') as target_file:
        target_file.write(content)

def replace_files_using_dict(file_mapping):
    """Replace the contents of target files with the contents of their corresponding source files using a dictionary."""
    for source, target in file_mapping.items():
        replace_file_content(source, target)
        print(f"Replaced content of {target} with content from {source}.")

# Example usage
file_mapping_dict = {
    "output/main.tf": "infrastructure/main.tf",
    "output/outputs.tf": "infrastructure/outputs.tf",
    "output/providers.tf": "infrastructure/providers.tf",
    "output/variables.tf": "infrastructure/variables.tf",
    "output/terraform.tfvars": "infrastructure/terraform.tfvars"
}

replace_files_using_dict(file_mapping_dict)


if __name__ == "__main__":
    main()
