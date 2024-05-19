#!usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user
     email: the email of the user
     password the password of the user
     firstname :
     and last name 
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)