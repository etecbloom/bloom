from argon2 import PasswordHasher, exceptions

ph = PasswordHasher (
    time_cost=3, 
    memory_cost=65536,
    parallelism=4,  
    hash_len=32,    
    salt_len=16 
)

def hash_password(password: str) -> str:
    if not password or not password.strip():
        raise ValueError("password cannot be empty")
    
    return ph.hash(password)

def verify_password(hashed: str, password: str) -> bool: 
    if not hashed or not password:
        raise ValueError("hash and password must be provided")
    
    try: 
        return ph.verify(hashed, password)
    except exceptions.VerifyMismatchError:
        return False