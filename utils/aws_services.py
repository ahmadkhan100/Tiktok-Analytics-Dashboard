import boto3
from botocore.exceptions import NoCredentialsError

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket_name: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
    except NoCredentialsError:
        print("Credentials not available")
        return False
    return True

def invoke_lambda_function(function_name, payload):
    """
    Invoke an AWS Lambda function

    :param function_name: Name of the Lambda function
    :param payload: Input payload for the function (dict)
    :return: Response from the Lambda function
    """
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=json.dumps(payload),
    )
    return response

# Example usage:
if __name__ == "__main__":
    # Upload a file to S3
    success = upload_file_to_s3('path/to/your/file.txt', 'your-bucket-name', 'optional-object-name.txt')
    if success:
        print("File uploaded successfully.")
    else:
        print("File upload failed.")

    # Invoke a Lambda function
    response = invoke_lambda_function('your-lambda-function-name', {'key': 'value'})
    print("Lambda response:", response)

