from dataclasses import dataclass


@dataclass
class CreateUserDTO:
    account: str
    email: str
    password: str
