from datetime import datetime, timedelta

from data.repopsitory.users_ import UserRepository


class UpdateUsage(UserRepository):

    def access_update_actually(self, user_id):
        if UserRepository()._is_user_exist(user_id):
            if not UserRepository()._is_admin_exist(user_id):
                last_update = self._last_update(user_id)
                print(last_update)
                if last_update is not None and last_update + timedelta(minutes=3) > datetime.now():
                    print("can do update")
                else:
                    print("can't do update. Wait for 3 minutes")
            else:
                # update immediately
                print("update immediately")
        else:
            print("You are not registered to get update. Input /start and register automatically")

