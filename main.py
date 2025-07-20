import os
import json

from utils import Utils
from encryptor import Encryptor
from rich.console import Console

console = Console()
utils = Utils()
VAULT_FILENAME = "vault.json"
users_dirs = os.path.join(os.getcwd(), 'users')


def create_user():
    utils.clear_terminal()
    utils.printTitle("Sign Up!")
    username = input("username: ").strip()
    password = input("password: ").strip()

    try:
        user_folder = os.path.join(users_dirs, username)
        os.makedirs(user_folder, exist_ok=True)

        user = Encryptor(user_folder=user_folder)
        encrypted_pass = user.encrypt(password)

        user_info = {
            "username": username,
            "password": encrypted_pass
        }

        with open(os.path.join(user_folder, VAULT_FILENAME), "w", encoding="utf-8") as f:
            json.dump(user_info, f)

        utils.printTitle(f"✅ User: {username} created successfully!")
        input("Press Enter to continue")
        return user_info

    except Exception as e:
        utils.logError(f"❌ Error during user creation: {e}")


def log_in():
    utils.clear_terminal()
    utils.printTitle("Log in")

    while True:
        username = input("username: ").strip()
        password = input("password: ").strip()

        try:
            user_folder = os.path.join(users_dirs, username)
            vault_path = os.path.join(user_folder, VAULT_FILENAME)

            if not os.path.exists(vault_path):
                utils.logError("❌ Incorrect username.")
                continue

            user = Encryptor(user_folder=user_folder)

            with open(vault_path, "r", encoding="utf-8") as f:
                user_info = json.load(f)

            decrypted_pass = user.decrypt(user_info["password"])

            if user_info.get("username") == username and decrypted_pass == password:
                utils.printTitle("✅ Logged in successfully!")
                input("Press Enter to continue")
                return user_info
            else:
                utils.logError("❌ Incorrect username or password.")

        except json.JSONDecodeError:
            utils.logError("❌ Error reading vault data")
        except Exception as e:
            utils.logError(f"❌ Unexpected error: {e}")


def add_password(user_info: dict):
    utils.clear_terminal()
    utils.printTitle("New password")

    site = input("Website: ").strip()
    site_username = input("username: ").strip()
    password = input("password: ").strip()

    try:
        user_folder = os.path.join(users_dirs, user_info["username"])
        vault_path = os.path.join(user_folder, VAULT_FILENAME)
        user = Encryptor(user_folder=user_folder)

        encrypted_pass = user.encrypt(password)

        with open(vault_path, "r", encoding="utf-8") as f:
            vault_data = json.load(f)

        vault_data[site] = {
            "username": site_username,
            "password": encrypted_pass
        }

        with open(vault_path, "w", encoding="utf-8") as f:
            json.dump(vault_data, f, indent=4)

        utils.printTitle("✅ Password added successfully!")
        input("Press Enter to continue")

    except FileNotFoundError:
        utils.logError("❌ Vault not found.")
    except json.JSONDecodeError:
        utils.logError("❌ Error reading vault data.")
    except Exception as e:
        utils.logError(f"❌ Unexpected error: {e}")


def view_password(user_info: dict):
    utils.clear_terminal()

    try:
        user_folder = os.path.join(users_dirs, user_info["username"])
        vault_path = os.path.join(user_folder, VAULT_FILENAME)
        user = Encryptor(user_folder=user_folder)

        with open(vault_path, "r", encoding="utf-8") as f:
            vault_data = json.load(f)

        site_keys = [key for key in vault_data if key not in ["username", "password"]]

        if not site_keys:
            utils.logWarning("⚠️ No sites saved yet.")
            input("Press Enter to continue")
        else:
            site = input("Website: ").strip()
            site_data = vault_data.get(site)
            if site_data:
                password = user.decrypt(site_data["password"])
                utils.printTitle(f"✅ Password for {site} is: {password}")
            else:
                utils.logError("❌ No password saved for this site.")

            input("Press Enter to continue")

    except FileNotFoundError:
        utils.logError("❌ Vault not found.")
    except json.JSONDecodeError:
        utils.logError("❌ Error reading vault data.")
    except Exception as e:
        utils.logError(f"❌ Unexpected error: {e}")


def view_saved_sites(user_info: dict):
    utils.clear_terminal()
    utils.printTitle("🔐 Saved Sites")

    try:
        user_folder = os.path.join(users_dirs, user_info["username"])
        vault_path = os.path.join(user_folder, VAULT_FILENAME)

        with open(vault_path, "r", encoding="utf-8") as f:
            vault_data = json.load(f)

        site_keys = [key for key in vault_data if key not in ["username", "password"]]

        if not site_keys:
            utils.logWarning("⚠️ No sites saved yet.")
        else:
            for i, site in enumerate(site_keys, 1):
                utils.printText(f"{i}. {site}")

        input("Press Enter to continue")

    except FileNotFoundError:
        utils.logError("]❌ Vault not found.")
    except json.JSONDecodeError:
        utils.logError("❌ Error reading vault data.")
    except Exception as e:
        utils.logError(f"❌ Unexpected error: {e}")


def main():
    utils.clear_terminal()
    utils.heading()
    utils.printTitle("Are you a new user? (y/n) 👀")
    newUser = input().strip()

    user = create_user() if newUser.lower() == "y" else log_in()

    while True:
        utils.choices()
        utils.printTitle("Enter your choice (1-4)")
        try:
            choice = int(input())
            utils.printTitle("====================================")
        except ValueError:
            utils.logError(f"❌ Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_password(user)
        elif choice == 2:
            view_password(user)
        elif choice == 3:
            view_saved_sites(user)
        elif choice == 4:
            utils.printTitle("👋 Exiting. Goodbye!")
            break
        else:
            utils.logError("🚨 Error 🚨 [!] Invalid choice")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        utils.logError(f"❌ Unexpected error: {e}")