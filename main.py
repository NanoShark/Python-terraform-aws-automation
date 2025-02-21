from user_input import get_user_inputs
from terraform_generator import generate_terraform_file
from aws_validator import fetch_aws_details
from terraform_actions import run_terraform, destroy_infrastructure
import os
import subprocess



def main() -> None:
    try:
        subprocess.run(["pip", "install", "-r", os.path.join(os.path.dirname(__file__), "requirements.txt")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")

    config = get_user_inputs()
    generate_terraform_file(config)
    run_terraform()
    fetch_aws_details()
    
    choice = input("Do you want to destroy the infrastructure? (yes/no): ").strip().lower()
    if choice == "yes":
         destroy_infrastructure()

if __name__ == "__main__":
    main()
