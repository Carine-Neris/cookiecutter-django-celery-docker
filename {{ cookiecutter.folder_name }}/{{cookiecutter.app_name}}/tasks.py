from celery import shared_task
import boto3
from carol.settings import DEBUG
from decouple import config
from botocore.client import Config



def download_aws(path):
    s3 = boto3.resource('s3',
                        aws_access_key_id=config('AWS_ACCESS_KEY'),
                        aws_secret_access_key=config('AWS_SECRET_KEY'),
                        config=Config(signature_version='s3v4'),
                        region_name='us-east-1')
    if DEBUG:
        s3.Bucket(config('AWS_BUCKET_NAME')).download_file(f'{path}', f'{path}')
    else:
        s3.Bucket(config('AWS_BUCKET_NAME')).download_file(f'{path[6:]}', f'{path}')




#Crie suas tasks aqui