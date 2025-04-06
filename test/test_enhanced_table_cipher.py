import unittest
from src.enhanced_table_cipher import EnhancedTableCipher

class TestEnhancedTableCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = EnhancedTableCipher("key")

    def test_encryption(self):
        plaintext = "hello"
        ciphertext = self.cipher.encrypt(plaintext)
        self.assertNotEqual(plaintext, ciphertext)

    def test_decryption(self):
        plaintext = "hello"
        ciphertext = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted)

    def test_encrypt_decrypt(self):
        plaintext = "python"
        ciphertext = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted)

    def test_empty_message(self):
        plaintext = ""
        ciphertext = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted)

    def test_message_with_spaces(self):
        plaintext = "hello world"
        ciphertext = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted)

if __name__ == '__main__':
    unittest.main()
