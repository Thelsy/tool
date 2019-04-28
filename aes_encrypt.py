#!/Users/lsy python
# coding:utf-8
# lsy
# AES ECB 加密工具类
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

# 计算text如果不足16的倍数则使用空格补充
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')

    # 加密函数
def encrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)
    cipher_text = cryptos.encrypt(text)
    code = b2a_hex(cipher_text)
    passwd = str(code).lstrip('b')
    return passwd[1:-1]

# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    cryptor = AES.new(key, mode)
    plain_text = cryptor.decrypt(a2b_hex(text))
    qd = bytes.decode(plain_text).rstrip('\0')
    return str(qd)