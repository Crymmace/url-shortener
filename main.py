import validators
from backend import Database
import random
import time

random.seed(time.time)

database = Database("urls.db")


def direction():
    task = input("What would you like to do? Encode or Decode? ").lower().strip().replace(" ", "")
    if task == "encode":
        url = input("Enter a URL: ")
        add_to_database(url)
    if task == "decode":
        url = input("Enter url: ")
        decode(url)


code = random.randint(0, 1000)


def add_to_database(entry):
    if validate(entry) and code not in database.search_all():
        key = code
        database.insert(entry, key)
        print(f"example.com/{key}")
    if not validate(entry):
        print("Please enter a valid URL")
        return False
    if validate(entry) and code in database.search_all():
        key = code
        database.insert(entry, key)
        print(f"example.com/{key}")


def find_entry(key):
    try:
        print(database.search(key=key)[0][1])
    except IndexError:
        print("Entry not found. Please try again.")


def decode(url):
    key = url.split("/")[-1]
    find_entry(key)


def validate(url):
    if validators.url(url):
        return True


direction()
