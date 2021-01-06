import unittest
import subcipher


class TestEncrypt(unittest.TestCase):
    def test_encrypt(self):
        ciphertext = subcipher.encrypt('hello there')
        self.assertEqual('svool gsviv', ciphertext)

        # This one doesn't work yet
        # ciphertext = subcipher.encrypt('Woah! punctuation?')
        # self.assertEqual('dlzs! kfmxgfzgrlm?', ciphertext)

        # or one with numbers
        # ciphertext = subcipher.encrypt('pi is about 3.14')
        # self.assertEqual('kr rh zylfg 3.14', ciphertext)

if __name__ == '__main__':
    unittest.main()
