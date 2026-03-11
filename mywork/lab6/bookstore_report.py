import os
from pymongo import MongoClient

MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")


def main():
    if not all([MONGODB_ATLAS_URL, MONGODB_ATLAS_USER, MONGODB_ATLAS_PWD]):
        print("Error: Please set MONGODB_ATLAS_URL, MONGODB_ATLAS_USER, and MONGODB_ATLAS_PWD environment variables.")
        return

    #connection string
    uri = f"mongodb+srv://{MONGODB_ATLAS_USER}:{MONGODB_ATLAS_PWD}@{MONGODB_ATLAS_URL}/?retryWrites=true&w=majority"

    #connect to MongoDB Atlas
    client = MongoClient(uri)

    try:
        #select database and collection
        db = client["bookstore"]
        authors_col = db["authors"]

        #total number of authors
        total_authors = authors_col.count_documents({})
        print(f"Total number of authors: {total_authors}\n")

        #iterate over authors
        print("Authors:")
        for author in authors_col.find({}, {"_id": 0, "name": 1, "nationality": 1, "birthday": 1, "bio.short": 1}):
            name = author.get("name", "Unknown")
            nationality = author.get("nationality", "Unknown")
            birthday = author.get("birthday", "N/A")
            bio_short = author.get("bio", {}).get("short", "")
            print(f"- {name} ({nationality}, Birthday: {birthday})")
            if bio_short:
                print(f"  Bio: {bio_short}")
        print("\nReport complete.")

    finally:
        client.close()


if __name__ == "__main__":
    main()