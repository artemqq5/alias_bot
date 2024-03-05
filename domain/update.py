from datetime import datetime, timedelta

from data.repopsitory.users_ import UserRepository


class UpdateUsage:

    @staticmethod
    def access_update_actually(user_id):
        if UserRepository()._is_user_exist(user_id):
            if not UserRepository()._is_admin_exist(user_id):
                last_update = UserRepository()._get_last_update(user_id)['last_update']
                if last_update is None or last_update + timedelta(minutes=3) < datetime.now():
                    UserRepository()._set_last_update(user_id, datetime.now())
                    print("can do update")
                else:
                    print("can't do update. Wait for 3 minutes")
            else:
                # update immediately
                print("update immediately")
        else:
            print("You are not registered to get update. Input /start and register automatically")
