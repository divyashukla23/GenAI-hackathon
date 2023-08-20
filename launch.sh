#!/bin/bash
echo "Setting up temporary credentials"
source assume-role.sh

# Detecting drift
cd ./infrastructure
./detect-drift.sh

# Generating code for the drift
cd ..
python3 main.py
