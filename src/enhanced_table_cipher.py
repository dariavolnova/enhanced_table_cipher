import argparse
import string


class EnhancedTableCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet = string.ascii_lowercase
        self.table = self._generate_table()

    def _generate_table(self):
        key_unique = ''.join(sorted(set(self.key), key=self.key.index))
        remaining_chars = ''.join([char for char in self.alphabet if char not in key_unique])
        return key_unique + remaining_chars

    def encrypt(self, plaintext):
        plaintext = plaintext.lower()
        ciphertext = ""

        for char in plaintext:
            if char in self.alphabet:
                idx = self.alphabet.index(char)
                ciphertext += self.table[idx]
            else:
                ciphertext += char

        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.lower()
        plaintext = ""

        for char in ciphertext:
            if char in self.table:
                idx = self.table.index(char)
                plaintext += self.alphabet[idx]
            else:
                plaintext += char

        return plaintext


def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using the enhanced table cipher.")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform: 'encrypt' or 'decrypt'")
    parser.add_argument("key", help="Key to generate the substitution table")
    parser.add_argument("message", help="Message to encrypt or decrypt")

    args = parser.parse_args()

    cipher = EnhancedTableCipher(args.key)

    if args.action == "encrypt":
        result = cipher.encrypt(args.message)
        print(f"Encrypted message: {result}")
    elif args.action == "decrypt":
        result = cipher.decrypt(args.message)
        print(f"Decrypted message: {result}")


if __name__ == "__main__":
    main()
