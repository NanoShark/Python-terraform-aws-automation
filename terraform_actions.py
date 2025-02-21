import os
from python_terraform import Terraform

def run_terraform() -> str:
    """Run terraform commands (init --> plan --> apply)."""
    terraform = Terraform(working_dir=os.path.dirname(__file__))
    try:
        return_code_init, stdout, stderr = terraform.init()
        if return_code_init != 0:
            raise Exception(f"Terraform Init Failed: {stderr}")
        print(stdout)

        return_code_plan, stdout, stderr = terraform.plan(capture_output=True)
        if return_code_plan != 0:
            raise Exception(f"Terraform Plan Failed: {stderr}")
        print(stdout)
        return_code_apply, stdout, stderr = terraform.apply(skip_plan=True, capture_output=True, auto_approve=True)
        if return_code_apply != 0:
            raise Exception(f"Terraform Apply Failed: {stderr}")
        #*******for testing purpose******#
        #terraform.destroy()
        #********************************#
        print(stdout)
    except Exception as e:
        print(f"Error executing Terraform: {e}")
        exit(1)

def destroy_infrastructure() -> None:
    """Run terraform command destroy."""
    tf = Terraform(working_dir=os.path.dirname(__file__))
    tf.destroy()
    print("Infrastructure Destroyed.")