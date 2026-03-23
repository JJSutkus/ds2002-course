import boto3
import argparse
import logging
import glob
import os

# setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder")
    parser.add_argument("destination")  # bucket/prefix
    args = parser.parse_args()
    return args.input_folder, args.destination


def upload(input_folder, destination):
    """Upload results*.csv files to S3"""
    try:
        s3 = boto3.client('s3')

        bucket, prefix = destination.split('/', 1)

        files = glob.glob(f"{input_folder}/results*.csv")

        for file in files:
            filename = os.path.basename(file)
            key = f"{prefix}/{filename}"

            logger.info(f"Uploading {filename}")
            s3.upload_file(file, bucket, key)

        return True

    except Exception as e:
        logger.error(f"Error: {e}")
        return False


def main():
    """Main function"""
    input_folder, destination = parse_args()

    success = upload(input_folder, destination)

    if success:
        logger.info("Upload successful")
    else:
        logger.error("Upload failed")


if __name__ == "__main__":
    main()