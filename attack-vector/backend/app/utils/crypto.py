import hashlib

def hash_flag(flag: str) -> str:
    # Constant-time safe comparison will be done on hashes
    return hashlib.sha256(flag.encode('utf-8')).hexdigest()
