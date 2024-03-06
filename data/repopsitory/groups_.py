from data.database_ import DefaultDataBase


class GroupRepository(DefaultDataBase):

    def _is_group_exist(self, group_id):
        COMMAND_ = '''select * from `groups` where `group_id` = %s;'''
        return self._select_one(COMMAND_, (group_id,))

    def _add_group(self, group_id, group_name, link):
        COMMAND_ = '''insert into `groups` values (%s, %s, %s);'''
        return self._insert(COMMAND_, (group_id, group_name, link))

    def _get_last_update(self, group_id):
        COMMAND_ = '''select `last_update` from `groups` where `group_id` = %s;'''
        return self._select_one(COMMAND_, (group_id,))

    def _set_last_update(self, group_id, last_update):
        COMMAND_ = '''update `groups` set `last_update` = %s where `group_id` = %s;'''
        return self._update(COMMAND_, (last_update, group_id))
