# This is needed to tell driftctl to use specific region for the scan
export AWS_DEFAULT_REGION="ap-south-1"
export AWS_REGION="ap-south-1"

# This command expects tfstate to be present in the local
# Need to change this to remote s3 bucket
# Outputs scan result in result.json
driftctl scan --output json://result.json