from data.config import USER_ADMIN_ID
from data.repopsitory.users_ import UserRepository


class AccessUsage:

    @staticmethod
    def change_user_access(param):
        if len(param) != 3:
            return "Wrong params. Try again"

        if UserRepository()._update_user_access(param[1], param[2]):
            return "User has successfully updated"
        else:
            return "Error when try update user"

