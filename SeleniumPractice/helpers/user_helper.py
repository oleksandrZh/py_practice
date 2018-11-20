class User:
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password


USER_NAME = "mngr163715"
USER_PASSWORD = "pUrereh"


def get_valid_user():
    user = User(USER_NAME, USER_PASSWORD)
    return user


def get_nonvalid_user():
    user = User(USER_NAME, "")
    return user
