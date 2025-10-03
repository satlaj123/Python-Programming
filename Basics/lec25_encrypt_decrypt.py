import base64
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import os, sys
from loguru import logger

# Configure loguru logger
logger.add("encryption.log", rotation="10 MB", level="DEBUG")

# Constants for encryption
try:
    # Initialize encryption parameters
    logger.debug("Initializing encryption parameters")
    key = "key1"
    iv = "my_username_pass"
    salt = "salt"

    if not (key and iv and salt):
        logger.error("Missing required encryption parameters")
        raise Exception(f"Error while fetching details for key/iv/salt")
except Exception as e:
    logger.error(f"Initialization error occurred: {str(e)}")
    sys.exit(0)

# Block size for AES encryption
BS = 16
# Padding functions for encryption
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s: s[0:-ord(s[-1:])]

def get_private_key():
    """Generate private key using PBKDF2"""
    try:
        logger.debug("Generating private key")
        Salt = salt.encode('utf-8')
        kdf = PBKDF2(key, Salt, 64, 1000)
        key32 = kdf[:32]
        logger.debug("Private key generated successfully")
        return key32
    except Exception as e:
        logger.error(f"Error generating private key: {str(e)}")
        raise

def encrypt(raw):
    """Encrypt the input string using AES encryption"""
    try:
        logger.debug(f"Attempting to encrypt data")
        raw = pad(raw)
        cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
        encrypted = base64.b64encode(cipher.encrypt(raw))
        logger.debug("Encryption completed successfully")
        return encrypted
    except Exception as e:
        logger.error(f"Encryption error: {str(e)}")
        raise

def decrypt(enc):
    """Decrypt the encrypted string using AES decryption"""
    try:
        logger.debug(f"Attempting to decrypt data")
        cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
        decrypted = unpad(cipher.decrypt(base64.b64decode(enc))).decode('utf8')
        logger.debug("Decryption completed successfully")
        return decrypted
    except Exception as e:
        logger.error(f"Decryption error: {str(e)}")
        raise

# Example usage
try:
    # Encrypt a sample password
    password = "manish"
    encrypted = encrypt(password)
    logger.info(f"Encrypted password = {encrypted}")
    
    # Uncomment to test decryption
    # decrypted = decrypt("U1AMRIQSTYosVJCmmqUHnA==")
    # logger.info(f"Decrypted text = {decrypted}")
except Exception as e:
    logger.error(f"Operation failed: {str(e)}")
