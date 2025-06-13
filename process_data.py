import os
from dotenv import load_dotenv
import boto3
import pandas as pd
from io import StringIO


load_dotenv()  # Load environment variables from .env file

#Retrieve AWS credentials from environment variables
ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION = os.getenv('AWS_REGION')
BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
FILE_KEY = "patient_data.csv"

# Connect to S3
s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION
)

# Download the CSV file from S3
obj = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
# Read the CSV file into a pandas DataFrame
df = pd.read_csv(obj['Body'])

#Analyze the data
print("\n Data Preview:")
print(df.head())

print("\n Average Age of Patients:", df["Age"].mean())
print("\n Chronic Conditions Distribution:")
print(df["ChronicCondition"].value_counts())