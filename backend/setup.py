#!/usr/bin/env python3
"""
Setup script for the Simple Web Agent backend.
This script installs the required dependencies and sets up Playwright browsers.
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Run a shell command and print the output."""
    print(f"\n{description}...")
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"✅ {description} completed successfully!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description.lower()}")
        print(f"Command failed with return code {e.returncode}")
        if e.stdout:
            print("\nSTDOUT:")
            print(e.stdout)
        if e.stderr:
            print("\nSTDERR:")
            print(e.stderr)
        return False

def main():
    print("🚀 Setting up Simple Web Agent Backend")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 9):
        print("❌ Python 3.9 or higher is required")
        sys.exit(1)
    
    # Install Python dependencies
    if not run_command(
        "pip install -r requirements.txt",
        "Installing Python dependencies"
    ):
        print("\n❌ Failed to install Python dependencies")
        sys.exit(1)
    
    # Install Playwright browsers
    if not run_command(
        "playwright install",
        "Installing Playwright browsers"
    ):
        print("\n❌ Failed to install Playwright browsers")
        sys.exit(1)
    
    # Create .env file if it doesn't exist
    if not os.path.exists(".env"):
        with open(".env.example", "r") as src, open(".env", "w") as dst:
            dst.write(src.read())
        print("\nℹ️  Created .env file from .env.example")
        print("   Please update the .env file with your configuration")
    
    print("\n✨ Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit the .env file and add your OpenAI API key")
    print("2. Start the backend server with: uvicorn main:app --reload")
    print("3. Access the API documentation at http://localhost:8000/docs")

if __name__ == "__main__":
    main()
