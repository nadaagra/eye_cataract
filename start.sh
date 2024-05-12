#!/bin/bash

# This script sets up and runs the Flask app for eye cataract detection.

# Exit immediately if any command fails
set -e

# Define virtual environment path
VIRTUALENV=".data/venv"

# Check if virtual environment directory exists
if [ ! -d "$VIRTUALENV" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv "$VIRTUALENV"
fi

# Check if pip is installed in virtual environment
if [ ! -f "$VIRTUALENV/bin/pip" ]; then
    echo "Installing pip in virtual environment..."
    curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | "$VIRTUALENV/bin/python"
fi

# Activate the virtual environment
source "$VIRTUALENV/bin/activate"

# Install required Python packages
echo "Installing dependencies..."
"$VIRTUALENV/bin/pip" install -r requirements.txt

# Run the Flask app
echo "Starting Flask app..."
"$VIRTUALENV/bin/python3" app.py
