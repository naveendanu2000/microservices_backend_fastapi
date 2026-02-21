from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def hashPassword(password: str) -> str:
    return password_hash.hash(password=password)


def verifyPassword(enteredPassword: str, savedPassword: str) -> bool:
    if password_hash.verify(enteredPassword, savedPassword):
        return True
    else:
        return False
