# 🔐 Password Vault

A terminal-based password manager built with Python. It allows users to securely store and retrieve their website credentials using symmetric encryption. Each user has a separate encrypted vault stored locally.

---

## 📦 Features

- ✅ Create user accounts with encrypted credentials
- 🔑 Add new passwords for websites
- 👁️ View stored passwords for any saved site
- 🧾 List all saved sites
- 🔒 Local file-based storage per user
- ✨ Rich terminal UI using `rich` module

---

## 🖥️ Tech Stack

- **Python 3**
- [`cryptography`](https://pypi.org/project/cryptography/) – AES encryption
- [`rich`](https://pypi.org/project/rich/) – for styled CLI interface
- [`pyfiglet`](https://pypi.org/project/pyfiglet/) – optional ASCII art titles

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/garys-demons/password_vault.git
cd password_vault
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the app
```bash
python main.py
```
---
## ⚠️ Disclaimer
This is an educational project and should not be used to store real-world passwords. No cloud syncing, password hashing, or 2FA is implemented.
