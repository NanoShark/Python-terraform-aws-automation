import json
import boto3
import os


def fetch_aws_details()-> None:
    """Validate EC2 instance and ALB using boto3."""
    try:
        ec2_client = boto3.client("ec2", region_name="us-east-1")
        elb_client = boto3.client("elbv2", region_name="us-east-1")
        
        instances = ec2_client.describe_instances().get("Reservations", [])
        instance_id, public_ip = None, None
        for reservation in instances:
            for instance in reservation.get("Instances", []):
                if instance.get("State", {}).get("Name") == "running":
                    instance_id = instance.get("InstanceId")
                    public_ip = instance.get("PublicIpAddress")
                    break
        
        lbs = elb_client.describe_load_balancers().get("LoadBalancers", [])
        lb_dns = lbs[0].get("DNSName") if lbs else None
        
        validation_data = {
            "instance_id": instance_id,
            "instance_state": "running" if instance_id else "not found",
            "public_ip": public_ip,
            "load_balancer_dns": lb_dns
        }

        output_path = os.path.join(os.path.dirname(__file__), "aws_validation.json")
        with open(output_path, "w") as json_file:
            json.dump(validation_data, json_file)
        
        return validation_data
    except Exception as e:
        print(f"Error fetching AWS details: {e}")
        