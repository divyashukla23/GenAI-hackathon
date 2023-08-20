# Terraform State Importer

## Goal

The major goal of this program is to reconcile resources in the cloud that have drifted from their original state. It does so by generating Terraform import commands that help align the actual state of the resources with the defined state in Terraform. This ensures that the configuration management is accurate and reflects the real-world state of the resources.

## Overview

Imagine you have a blueprint (plan) that describes how a building should look, but over time, changes have been made to the building that are not reflected in the blueprint. This program serves as a tool to update the blueprint to match the actual state of the building.

In the context of cloud computing, the "blueprint" is a configuration file that describes how resources (like virtual machines, databases, etc.) should be configured. Sometimes, these resources might be changed manually or by other means, leading to a difference between the actual state and the blueprint. This program helps to align them back.

## Prerequisites

Before using the Terraform State Importer, make sure you have the following programs and permissions set up:

1. **Python 3**: You should have Python 3 installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Terraform**: Install Terraform on your system by following the instructions in the [Terraform documentation](https://learn.hashicorp.com/tutorials/terraform/install-cli).

3. **AWS CLI**: You should have the AWS Command Line Interface (CLI) installed and configured with valid credentials to access your AWS account.

4. **IAM Role**: Create an IAM role named `HackathonAdmin` in your AWS account with the necessary permissions. This role will be assumed by the `assume-role.sh` script. Alternatively, if you already have IAM role, update ARN in `assume-role.sh`

## How to Use
Simply run `./launch.sh` in your terminal, and it will take care of setting up and executing the entire process.

## How the Program Works

1. **Reading the Drifted State**: The program takes a JSON file that lists the resources that have drifted from their original state. This information includes what the resources are and how they have changed.

2. **Generating Commands**: For each drifted resource, the program constructs a command that tells Terraform (a popular infrastructure management tool) how to align the actual state with the desired state.

3. **Creating a Script**: The commands are saved into a shell script file (`command.sh`), along with initial setup instructions like initializing Terraform.

4. **Creating Terraform Blocks**: The program also creates a Terraform file (`main.tf`) that includes the necessary resource definitions to match the current state.

5. **Executing the Script**: The program then runs the generated shell script, executing the Terraform commands to import the drifted resources back into alignment with the defined state.

6. **Cleaning Up**: Finally, the temporary files (`command.sh` and `main.tf`) used in the process are deleted.

## How to Use

Place the JSON file containing the information about the drifted resources in the same directory as the program and name it `result.json`. Then, run the program, and it will take care of the rest.

## Conclusion

This tool is useful for maintaining consistency and accuracy in managing cloud resources. By ensuring that the defined state matches the actual state, it helps prevent unexpected behavior and makes the management of these resources more reliable and predictable.

---

Feel free to modify or expand this README as needed to match your specific requirements and context!

---

Made with ❤️ by **GenDev Squad**