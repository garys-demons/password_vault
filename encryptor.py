from cryptography.fernet import Fernet
import os

class Encryptor:
    def __init__(self, user_folder):
        self.key_path = os.path.join(user_folder, "key.key")
        self.key = self.load_or_create_key()
        self.fernet = Fernet(self.key)

    def load_or_create_key(self):
        if os.path.exists(self.key_path):
            with open(self.key_path, 'rb') as f:
                return f.read()
        else:
            new_key = Fernet.generate_key()
            with open(self.key_path, 'wb') as f:
                f.write(new_key)
            return new_key

    def encrypt(self, plaintext: str) -> str:
        encrypted = self.fernet.encrypt(plaintext.encode())
        return encrypted.decode()

    def decrypt(self, ciphertext: str) -> str:
        decrypted = self.fernet.decrypt(ciphertext.encode())
        return decrypted.decode()
