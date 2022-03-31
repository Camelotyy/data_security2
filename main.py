# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')



from Cryptodome.Cipher import DES

import binascii

key = b'abcdefgh'

des = DES.new(key, DES.MODE_ECB)
text = 'NCUT'

text = text + (8-(len(text) % 8)) * '='

encrypto_text = des.encrypt(text.encode())

print(binascii.b2a_hex(encrypto_text))

decrypto_text = des.decrypt(encrypto_text)

print(decrypto_text)