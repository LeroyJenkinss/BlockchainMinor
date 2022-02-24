import string
import cryptography
import gmpy2

class encrypt:
    def simple_rsa_encrypt(self, m, publickey):
        # Public_numbers returns a data structure with the 'e' and 'n' parameters.
        numbers = publickey.public_numbers()

        # Encryption is(m^e) % n.
        return gmpy2.powmod(m, numbers.e, numbers.n)

    def simple_rsa_decrypt(self, c, privatekey):
       # Private_numbers returns a data structure with the 'd' and 'n' parameters.
       numbers = privatekey.private_numbers()

       # Decryption is(c^d) % n.
       return gmpy2.powmod(c, numbers.d, numbers.public_numbers.n)

    def int_to_bytes(i):
        i = int(i)
        return i.to_bytes((i.bit_length() + 7) // 8, byteorder="big")

    def bytes_to_int(b):
        return int.from_bytes(b, byteorder="big")