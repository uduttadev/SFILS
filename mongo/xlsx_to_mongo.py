import pandas
from pymongo import MongoClient

def main():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["SFILS"] 
    collection = db["LibraryUsage"]
    collection.delete_many({})
    create_indexes(collection)


    df = pandas.read_excel("SFPL_DataSF_library-usage_Jan_2023.xlsx")

    records = df.to_dict(orient="records")

    result = collection.insert_many(records)
    print(f"Inserted {len(result.inserted_ids)} documents into MongoDB.")

def create_indexes(collection):
    collection.create_index("home_library_code")
    collection.create_index("patron_type_code")



if __name__ == "__main__":
    main()

