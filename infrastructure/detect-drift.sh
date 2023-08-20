# This is needed to tell driftctl to use specific region for the scan
export AWS_DEFAULT_REGION="ap-south-1"
export AWS_REGION="ap-south-1"

echo "Scanning drifts in region $AWS_DEFAULT_REGION for unmanaged resources"
# This command expects tfstate to be present in the local
# Outputs scan result in result.json
driftctl scan --output json://result.json
echo "Scanning complete"
cp result.json ../result.json
echo "Results are stored in result.json file in root folder"