from data.database_ import DefaultDataBase


class UserRepository(DefaultDataBase):

    def is_admin(self, userid):
        COMMAND_ = '''select * from `users` where `userid` = %s;'''
        return self._insert(COMMAND_, (userid,))

