from typing import Dict

def get_user_inputs() -> Dict[str, str]:
    """Prompt user for cloud deployment configurations."""
    ami_options = {
        "ubuntu": "ami-0dee1ac7107ae9f8c",
        "amazon-linux": "ami-0f1a6835595fb9246"
    }
    instance_types = {"small": "t3.small", "medium": "t3.medium"}
    
    ami_choice = input("Choose AMI (ubuntu/amazon-linux): ").strip().lower()
    instance_choice = input("Choose instance type (small/medium): ").strip().lower()
    region = input("Enter AWS region (Only us-east-1 allowed): ").strip()
    lb_name = input("Enter Load Balancer name: ").strip()
    
    if region != "us-east-1":
        print("Invalid region, defaulting to us-east-1.")
        region = "us-east-1"
    
    return {
        "ami": ami_options.get(ami_choice, "ami-12345678"),
        "instance_type": instance_types.get(instance_choice, "t3.small"),
        "region": region,
        "load_balancer_name": lb_name,
        "availability_zone": "us-east-1a"
    }
