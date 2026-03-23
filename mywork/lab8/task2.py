import boto3
import os

# Configuration
REGION = "us-east-1"
BUCKET_NAME = "ds2002-<yourid>"   # CHANGE THIS
PRIVATE_FILE = "private.jpg"
PUBLIC_FILE = "public.jpg"


def list_buckets(s3):
    """List all S3 buckets"""
    response = s3.list_buckets()
    print("Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")
    print()


def upload_private(s3):
    """Upload a private file"""
    
    s3.put_object(
        Body=open(PRIVATE_FILE, 'rb'),
        Bucket=BUCKET_NAME,
        Key=PRIVATE_FILE
    )

    print(f"Uploaded PRIVATE file: {PRIVATE_FILE}")
    print(f"Test URL (should fail):")
    print(f"https://s3.amazonaws.com/{BUCKET_NAME}/{PRIVATE_FILE}\n")


def upload_public(s3):
    """Upload a public file"""

    s3.put_object(
        Body=open(PUBLIC_FILE, 'rb'),
        Bucket=BUCKET_NAME,
        Key=PUBLIC_FILE,
        ACL='public-read'
    )

    print(f"Uploaded PUBLIC file: {PUBLIC_FILE}")
    print(f"Test URL (should work):")
    print(f"https://s3.amazonaws.com/{BUCKET_NAME}/{PUBLIC_FILE}\n")


def main():
    """Main execution function"""
    s3 = boto3.client('s3', region_name=REGION)

    print("=== TASK 2: S3 WITH BOTO3 ===\n")

    list_buckets(s3)
    upload_private(s3)
    upload_public(s3)

    print("Done.")


if __name__ == "__main__":
    main()