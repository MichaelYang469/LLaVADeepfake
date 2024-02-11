#!/bin/bash

# Path to the Python script
PYTHON_SCRIPT="/mnt/user/myang/LLaVA-2/my_code/python/qloraprep.py"

# Main directory containing subdirectories with image files
MAIN_DIRECTORY="/mnt/user/myang/OneDrive_1_9-6-2023/facial_attributes/images/train/"

# Path to save the JSON files
JSON_OUTPUT_DIR="/mnt/user/myang/LLaVA-2/my_code/json/qlorajson"

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Python script not found: $PYTHON_SCRIPT"
    exit 1
fi

# Check if the main directory exists
if [ ! -d "$MAIN_DIRECTORY" ]; then
    echo "Error: Main directory not found: $MAIN_DIRECTORY"
    exit 1
fi

# Loop through each subdirectory in the main directory
for SUBDIRECTORY in "$MAIN_DIRECTORY"/*/; do
    # Check if the subdirectory contains image files
    if [ -d "$SUBDIRECTORY" ]; then
        # Run the Python script with the specified arguments
        python3 "$PYTHON_SCRIPT" "$SUBDIRECTORY" "$JSON_OUTPUT_DIR"
        echo "Processing directory: $SUBDIRECTORY"
    fi
done
