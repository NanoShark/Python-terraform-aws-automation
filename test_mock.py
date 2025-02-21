# Import the required functions
from aws_validator import fetch_aws_details
from unittest.mock import patch

# Mock the EC2 client function
def mock_ec2_client():
    return {
        "Reservations": [
            {
                "Instances": [
                    {
                        "InstanceId": "i-0a1b2c3d4e5f6g7h8",
                        "State": {"Name": "running"},
                        "PublicIpAddress": "54.123.45.67"  
                    },
                    {
                        "InstanceId": "i-0a1b2c3d4e5f6g7h9",
                        "State": {"Name": "stopped"},
                    }
                ]
            }
        ]
    }


def mock_elb_client():
    return {
        "LoadBalancers": [
            {
                "DNSName": "my-load-balancer-12345678.us-east-1.elb.amazonaws.com"
            }
        ]
    }


def mock_fetch_ec2_detailes():
    ec2_client = mock_ec2_client()
    instance_id = None
    public_ip = None
    instances = ec2_client["Reservations"]
    
    for res in instances:
        for instance in res["Instances"]:
            if instance["State"]["Name"] == "running":
                instance_id = instance["InstanceId"]
                public_ip = instance.get("PublicIpAddress", "N/A")  # .get() safely retrieves the value or returns "N/A"
                break
    
    if instance_id:
        instance_state = "running"
    else:
        instance_state = "not found"
    
    return instance_id, public_ip, instance_state


def mock_fetch_lbs_detailes():
    elb_client = mock_elb_client()
    lbs = elb_client["LoadBalancers"]
    
    if lbs:
        lb_dns = lbs[0]["DNSName"]
    else:
        lb_dns = None
    
    return lb_dns


fetch_aws_details() 