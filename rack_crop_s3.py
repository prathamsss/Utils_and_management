# Import the necessary packages
import os
import boto3
from pprint import pprint

class StorageManagement:
    """
    A class to manage S3 storage operations.
    """

    def __init__(self):
        """
        Initializes an instance of the class with an S3 client.
        """
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
            region_name=os.environ['AWS_REGION'],
            endpoint_url=os.environ['AWS_ENDPOINT_URL']
        )

    def get_all_buckets(self):
        """
        Returns a list of all buckets in S3.

        :return: A list of dictionaries representing the buckets.
        :rtype: list
        """
        return self.s3.list_buckets()

    def get_files(self, bucket_name):
        """
        Returns a list of all files in the specified bucket.

        :param bucket_name: The name of the S3 bucket to retrieve files from.
        :type bucket_name: str
        :return: A list of dictionaries representing the files.
        :rtype: list
        """
        response = self.s3.list_objects(Bucket=bucket_name, MaxKeys=10)
        return response

    def upload_file(self, bucket_name, local_file_path, key_name):
        """
        Uploads a file to the specified S3 bucket.

        :param bucket_name: The name of the S3 bucket to upload the file to.
        :type bucket_name: str
        :param local_file_path: The path of the local file to upload.
        :type local_file_path: str
        :param key_name: The name to assign to the file in S3.
        :type key_name: str
        """
        self.s3.upload_file(Filename=local_file_path, Bucket=bucket_name, Key=key_name)

    def download_file(self, bucket_name, key_name, local_file_path):
        """
        Downloads a file from the specified S3 bucket to the local file system.

        :param bucket_name: The name of the S3 bucket to download the file from.
        :type bucket_name: str
        :param key_name: The name of the file in S3 to download.
        :type key_name: str
        :param local_file_path: The path of the local file to save the downloaded file to.
        :type local_file_path: str
        """
        self.s3.download_file(Bucket=bucket_name, Key=key_name, Filename=local_file_path)


s3 = StorageManagement()
#
# download_dir = "/Users/prathameshsardeshmukh/Desktop/infinimum robotics/s3_data"
# bucket_name = "trail"
# local_file_path = "/Users/prathameshsardeshmukh/Desktop/infinimum robotics/img1.png"
# key_name = "i2"

# s3.upload_file(bucket_name,local_file_path,key_name)

pprint(s3.get_files("trail"))

# s3.dowonload_file(bucket_name,"img1.png",key_name)