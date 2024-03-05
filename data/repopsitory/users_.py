from data.database_ import DefaultDataBase


class UserRepository(DefaultDataBase):

    def _is_admin_exist(self, user_id):
        COMMAND_ = '''select * from `users` where `user_id` = %s and `role` = 'admin';'''
        return self._select(COMMAND_, (user_id,))

    def _is_user_exist(self, user_id):
        COMMAND_ = '''select * from `users` where `user_id` = %s;'''
        return self._select(COMMAND_, (user_id,))

    def _add_user(self, user_id, username, first_name, last_name):
        COMMAND_ = '''insert into `users`(`user_id`, `username`, `first_name`, `last_name`) values (%s, %s, %s, %s);'''
        return self._insert(COMMAND_, (user_id, username, first_name, last_name))

    def _last_update(self, user_id):
        COMMAND_ = '''select `last_update` from `users` where `user_id` = %s;'''
        return self._select(COMMAND_, (user_id,))
