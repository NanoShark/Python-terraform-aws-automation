# Python Exam

## Overview
This project automates the deployment of an AWS EC2 instance attached to an Application Load Balancer (ALB) using Terraform, Python, and Boto3. The infrastructure is dynamically generated using Jinja2 templates, executed via Terraform, and validated using AWS APIs.

## Features
- **Dynamic Terraform Configuration**: Uses Jinja2 templating to generate Terraform scripts.
- **Automated Deployment**: Terraform execution is managed through Python.
- **AWS Resource Validation**: Uses Boto3 to confirm EC2 instance and ALB deployment.
- **Error Handling & Modularization**: Functions and classes are well-structured with exception handling.
- **Infrastructure Cleanup**: Ability to destroy Terraform-managed resources when no longer needed.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Terraform
- AWS CLI (configured with credentials)


## Installation
First, clone the repository. No need to worry about dependencies—just run the script, and it will take care of installing everything you need.

## Usage
### Step 1: Configure AWS Credentials
Ensure AWS credentials are set up using the AWS CLI:
```sh
aws configure
```

### Step 2: Run the Script
Execute the main script to start the deployment:
```sh
python main.py
```
You will be prompted to enter:
- AMI selection (Ubuntu or Amazon Linux)
- Instance type (t3.small/t3.medium)
- Load Balancer name

### Step 3: Validate Deployment
After successful execution, the script generates `aws_validation.json` with details of the deployed resources:
```json
{
    "instance_id": "i-0123456789abcdef0",
    "instance_state": "running",
    "public_ip": "3.92.102.45",
    "load_balancer_dns": "my-alb-123456.elb.amazonaws.com"
}
```

### Step 4: Destroy Infrastructure
To terminate all resources, select `yes` when prompted at the end of the execution, or manually run:
```sh
terraform destroy
```

## Project Structure
```
├── main.py                 # Main execution script
├── user_input.py           # Handles user input
├── terraform_generator.py  # Generates Terraform files
├── terraform_actions.py    # Executes Terraform commands
├── aws_validator.py        # Validates AWS resources
├── requirements.txt        # Required Python packages
├── test_mock.py            # Test Aws validation
└── README.md               # Project documentation
```

## Error Handling
- Handles invalid AWS regions, Terraform execution failures, and AWS API errors.
- Uses `try-except` blocks for better reliability.


