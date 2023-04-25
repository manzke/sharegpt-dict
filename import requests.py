import urllib.request

# List of shared session IDs to test
similar_shared_session_ids = [
    "4qj1DB0",
    "Fe2keKv",
    "GBzRdCM",
    "oPt72P3",
    "v8GHE1c",
    "GPhnDms",
    "jGKq34x",
    "dds1LKN",
    "ICZsSl7",
    "3aBcDeF",
    "7gHiJkL",
    "9mNoPqR",
    "2sTuVwX",
    "6yZaBcD",
    "8eFgHiJ",
    "4kLmNoP",
    "1qRsTuV",
    "5wXyZaB",
    "0cDeFgH",
    "3iJkLmN",
    "7oPqRsT",
    "9uVwXyZ",
    "2aBcDeF",
    "6gHiJkL",
    "8mNoPqR",
    "4sTuVwX",
    "1yZaBcD",
    "5eFgHiJ",
    "0kLmNoP",
    "3qRsTuV",
    "7wXyZaB",
    "9cDeFgH",
    "2iJkLmN",
    "6oPqRsT",
    "8uVwXyZ",
    "4aBcDeF",
    "1gHiJkL",
    "5mNoPqR",
    "0sTuVwX",
    "3yZaBcD",
    "7eFgHiJ",
    "9kLmNoP",
    "2qRsTuV",
    "6wXyZaB",
    "8cDeFgH",
    "4iJkLmN",
    "1oPqRsT",
    "5uVwXyZ",
    "0aBcDeF",
    "3gHiJkL",
    "7mNoPqR",
    "9sTuVwX",
    "2yZaBcD",
    "6eFgHiJ",
    "8kLmNoP",
    "4qRsTuV",
    "1wXyZaB",
]

# Base URL
base_url = "https://sharegpt.com/c/"

# Loop through each shared session ID and send HTTP request to check existence
for session_id in similar_shared_session_ids:
    url = base_url + session_id
    try:
        response = urllib.request.urlopen(url)
        print(f"{session_id}: Exists")  # Print if exists
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"{session_id}: Does not exist")  # Print if does not exist