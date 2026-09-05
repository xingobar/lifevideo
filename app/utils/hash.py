from pwdlib import PasswordHash

_pwd_hash = PasswordHash.recommended()


def hash_password(plain: str) -> str:
    return _pwd_hash.hash(plain)


def verify_password(plain: str, hashed: str) -> bool:
    return _pwd_hash.verify(plain, hashed)
