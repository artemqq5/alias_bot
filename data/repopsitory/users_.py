from data.database_ import DefaultDataBase


class UserRepository(DefaultDataBase):

    def _is_admin_exist(self, user_id):
        COMMAND_ = '''select * from `users` where `user_id` = %s and `role` = 'admin';'''
        return self._select_one(COMMAND_, (user_id,))

    def _is_user_exist(self, user_id):
        COMMAND_ = '''select * from `users` where `user_id` = %s;'''
        return self._select_one(COMMAND_, (user_id,))

    def _add_user(self, user_id, username, first_name, last_name):
        COMMAND_ = '''insert into `users`(`user_id`, `username`, `first_name`, `last_name`) values (%s, %s, %s, %s);'''
        return self._insert(COMMAND_, (user_id, username, first_name, last_name))

    def _get_last_update(self, user_id):
        COMMAND_ = '''select `last_update` from `users` where `user_id` = %s;'''
        return self._select_one(COMMAND_, (user_id,))

    def _set_last_update(self, user_id, last_update):
        COMMAND_ = '''update `users` set `last_update` = %s where `user_id` = %s;'''
        return self._update(COMMAND_, (last_update, user_id))

    def _update_user_access(self, user_id, access):
        COMMAND_ = '''update `users` set `role` = %s where `user_id` = %s;'''
        return self._update(COMMAND_, (access, user_id))
