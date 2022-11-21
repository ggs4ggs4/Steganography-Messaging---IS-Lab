import math
import random


def is_prime(number):
    ''' test primality of number (odd integer) '''
    
    limit = math.floor(math.sqrt(number)) + 1
    for divisor in range(3, limit, 2):
        if(number % divisor == 0):
            return 0
    else:
        return 1

        
def gcd(a, b):
    ''' compute greatest commmon divisor of a and b '''
    
    while(a % b):
        a, b = b, a % b
    return b


def inverse(number, base):
    ''' find the multiplicative inverse of number modulo base '''
    
    a, b = number, base
    stack = []
    
    while(True):
        a, q, b = b, a // b, a % b
        if(b):
            stack.append(q)
        else:
            break
    
    x, y = 0, 1    
    while(len(stack)):
        q = stack.pop()
        x, y = y, x + y * -q
        
    return x % base


def generate_key(bit_count=6):
    ''' generate a pair of keys; private key: (d, n)  and public key: (e, n) '''
    
    while(True):
        p = (random.randrange(2 ** (bit_count - 1) + 1, 2 ** bit_count, 2))
        if(is_prime(p)):
            break
    
    while(True):
        q = (random.randrange(2 ** (bit_count - 1) + 1, 2 ** bit_count, 2))
        if(q != p and is_prime(q)):
            break
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    while(True):
        e = random.randrange(2, phi_n)
        if(gcd(e, phi_n) == 1):
            break
        
    d = inverse(e, phi_n)
    return (d, n), (e, n)

    
def e(char_plain, public_key):
    ''' encrypt char_plain using public_key (e, n) '''
    
    e, n = public_key[0], public_key[1]
    block_cipher = chr(pow(ord(char_plain), e) % n)
    return block_cipher


def d(block_cipher, private_key):
    ''' decrypt block_cipher using private_key (d, n) '''
    
    d, n = private_key[0], private_key[1]
    char_plain = chr(pow((ord(block_cipher )% n), d) % n)
    return char_plain

def encrypt(plaintext,public_key):
    cypher=""
    for i in plaintext:
        cypher+=e(i,public_key)
    return cypher

def decrypt(cypher,private_key):
    plaintext=""
    for i in cypher:
        plaintext+=d(i,private_key)
    return plaintext