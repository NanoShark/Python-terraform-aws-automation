from typing import Dict
from jinja2 import Template
import os

def generate_terraform_file(config: Dict[str, str]) -> None:
    """Generate Terraform file from Jinja2 template."""

    # ami = config.get("ami")
    # instance_type = config.get("instance_type")
    # region = config.get("region")
    # load_balancer_name = config.get("load_balancer_name")
    # availability_zone = config.get("availability_zone")
    
    terraform_template = """
provider "aws" {
 region = "{{ region }}"
}

resource "aws_instance" "web_server" {
 ami = "{{ ami }}"
 instance_type = "{{ instance_type }}"
 availability_zone = "{{ availability_zone }}"

 tags = {
   Name = "WebServer"
 }
}

resource "aws_lb" "application_lb" {
 name = "{{ load_balancer_name }}"
 internal = false
 load_balancer_type = "application"
 security_groups = [aws_security_group.lb_sg.id]
 subnets = aws_subnet.public[*].id
}

resource "aws_security_group" "lb_sg" {
 name        = "lb_security_group"
 description = "Allow HTTP inbound traffic"

 ingress {
   from_port   = 80
   to_port     = 80
   protocol    = "tcp"
   cidr_blocks = ["0.0.0.0/0"]
 }
}

resource "aws_lb_listener" "http_listener" {
 load_balancer_arn = aws_lb.application_lb.arn
 port              = 80
 protocol          = "HTTP"

 default_action {
   type             = "forward"
   target_group_arn = aws_lb_target_group.web_target_group.arn
 }
}

resource "aws_lb_target_group" "web_target_group" {
 name     = "web-target-group"
 port     = 80
 protocol = "HTTP"
 vpc_id   = aws_vpc.main.id
}

resource "aws_lb_target_group_attachment" "web_instance_attachment" {
 target_group_arn = aws_lb_target_group.web_target_group.arn
 target_id        = aws_instance.web_server.id
}

resource "aws_subnet" "public" {
 count = 2
 vpc_id = aws_vpc.main.id
 cidr_block = "10.0.${count.index}.0/24"
 availability_zone = element(["us-east-1a", "us-east-1b"], count.index)
}

resource "aws_vpc" "main" {
 cidr_block = "10.0.0.0/16"
}
"""

    template = Template(terraform_template)
    terraform_config = template.render(config)
    
    output_path = os.path.join(os.path.dirname(__file__), "main.tf")
    with open(output_path, "w") as terraform_file:
        terraform_file.write(terraform_config)