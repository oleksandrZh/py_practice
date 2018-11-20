class Manager:
    def __init__(self, user_name, user_password):
        if user_name is not None:
            self.user_name = user_name
        if user_password is not None:
            self.user_password = user_password


USER_NAME = "mngr163715"
USER_PASSWORD = "pUrereh"


def get_valid_manager():
    user = Manager(USER_NAME, USER_PASSWORD)
    return user


def get_nonvalid_user():
    user = Manager(USER_NAME, "")
    return user
