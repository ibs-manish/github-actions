import os
import boto3

# env variables
max_number_tries = 10
job = os.getenv("JOB") if(os.getenv("JOB")) else None
aws_region = os.getenv('AWS_REGION') if(os.getenv('AWS_REGION')) else None
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID') if ( os.getenv('AWS_ACCESS_KEY_ID') ) else None
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY') if(os.getenv('AWS_SECRET_ACCESS_KEY')) else None
instance_id = os.getenv('INSTANCE_ID') if(os.getenv('INSTANCE_ID')) else None

#making checks for essential variables
assert job,                   "Must Provide job_name for this workflow"
assert aws_region ,           "Must Provide aws_region for this workflow"
assert aws_access_key_id,     "Must Provide aws_access_key_id for this workflow"
assert aws_secret_access_key, "Must Provide aws_secret_access_key for this workflow"
assert instance_id,           "Must Provide instance_id for this workflow"

#initiating boto3
SSM = boto3.client('ssm', region_name=aws_region)

def main():
    # running jobs
    if job == "AWS_SSM":
        aws_ssm_send_command()
    else:
        raise ValueError("Please provide Valid JOB Name")
    

def aws_ssm_send_command():
    print("---------------running aws_ssm_send_command---------------")

    response = boto3.client('ec2', 
                            aws_access_key_id=aws_access_key_id, 
                            aws_secret_access_key=aws_secret_access_key , 
                            region_name=aws_region
                            ).describe_instances(
        MaxResults=123
    )
    print(response)

if __name__ == "__main__":
    main()