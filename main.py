import os
import json
from crypto_utils import derive_key, encrypt_password, decrypt_password

SALT_FILE = "salt.bin"
DATA_FILE = "passwords.json"

def get_or_create_salt():
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            return f.read()
    else:
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
        return salt

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def add_password(key, data):
    site = input("Enter website/app name: ")
    password = input("Enter password to save: ")
    encrypted = encrypt_password(password, key)
    data[site] = encrypted.decode()  # store as string so it can go in JSON
    save_data(data)
    print(f"Password for {site} saved!")

def view_password(key, data):
    site = input("Enter website/app name to view: ")
    if site not in data:
        print("No entry found for that site.")
        return
    encrypted = data[site].encode()  # convert back to bytes
    decrypted = decrypt_password(encrypted, key)
    print(f"Password for {site}: {decrypted}")

def main():
    salt = get_or_create_salt()
    master_password = input("Enter your master password: ")
    key = derive_key(master_password, salt)
    data = load_data()

    while True:
        print("\n1. Add password")
        print("2. View password")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_password(key, data)
        elif choice == "2":
            view_password(key, data)
        elif choice == "3":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
