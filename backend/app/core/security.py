from argon2 import PasswordHasher, exceptions
import re

ph = PasswordHasher (
    time_cost=3, 
    memory_cost=65536,
    parallelism=4,  
    hash_len=32,    
    salt_len=16 
)

# ------------------------------- This function validates certain standards that passwords must have. -----------------------

def validate_password(password: str) -> None:
    if len(password) < 10:
        raise ValueError("Password cannot be less than 8 characters")
    
    if not any(c.isupper() for c in password):
        raise ValueError("The password must contain at least one uppercase letter")
    
    if not any(c.isdigit() for c in password):
        raise ValueError("The password must contain a number.")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValueError("The password must contain a special character")

# ---------------------- This function hashes the password so that it is not exposed in the database. ------------------------

def hash_password(password: str) -> str:
    if not password or not password.strip():
        raise ValueError("password cannot be empty")

    validate_password(password)

    return ph.hash(password)

# --------- This function supports login by comparing the hashed password with the password entered by the user. -------------

def verify_password(hashed: str, password: str) -> bool: 
    if not hashed or not password:
        raise ValueError("hash and password must be provided")
    
    try: 
        return ph.verify(hashed, password)
    except exceptions.VerifyMismatchError:
        return False