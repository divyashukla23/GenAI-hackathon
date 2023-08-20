# This is needed to tell driftctl to use specific region for the scan
export AWS_DEFAULT_REGION="ap-south-1"
export AWS_REGION="ap-south-1"

# This command expects tfstate to be present in the local
# Need to change this to remote s3 bucket
# Outputs scan result in result.json
echo "Scanning cloud for unmanaged resources"
driftctl scan --output json://result.json
echo "Scanning complete"
cp result.json ../result.json
echo "Results are stored in result.json file in root folder"