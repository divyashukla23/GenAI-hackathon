#!/bin/bash

# unset previously expired sessions
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN

# Assuming the role and capturing the JSON output
output=$(aws sts assume-role --role-arn arn:aws:iam::462066733505:role/HackathonAdmin --role-session-name TerraformSession)

# Extracting individual credentials from the output and setting them as environment variables
export AWS_ACCESS_KEY_ID=$(echo $output | jq -r .Credentials.AccessKeyId)
export AWS_SECRET_ACCESS_KEY=$(echo $output | jq -r .Credentials.SecretAccessKey)
export AWS_SESSION_TOKEN=$(echo $output | jq -r .Credentials.SessionToken)

echo "Temporary credentials set for session."
