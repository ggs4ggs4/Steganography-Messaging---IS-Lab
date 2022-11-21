
from rsa import*
print(encrypt("hello how are you",(88597,139949)))
print(decrypt(encrypt("hello how are you",(88597,139949)),(137533,139949)))