from data.database_ import DefaultDataBase


class ChatRepository(DefaultDataBase):

    def add_chat(self, chatid, title, link):
        COMMAND_ = '''insert into `chats` (`chatid`, `title`, `link`) values(%s, %s, %s);'''
        return self._insert(COMMAND_, (chatid, title, link))

    def is_exists(self, chatid):
        COMMAND_ = '''select * from `chats` where `chatid` = %s;'''
        return self._select(COMMAND_, (chatid,))
