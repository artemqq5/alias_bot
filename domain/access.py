from data.config import USER_ADMIN_ID
from data.repopsitory.users_ import UserRepository


class AccessUsage:

    @staticmethod
    def change_user_access(param):
        if len(param) != 3:
            return "Wrong params. Try again"

        if not UserRepository()._is_user_exist(param[1]):
            return "User is not start the bot in private chat"

        if UserRepository()._update_user_access(param[1], param[2]):
            return "User has successfully updated"
        else:
            return "Error when try update user"

