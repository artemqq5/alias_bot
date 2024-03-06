from datetime import datetime, timedelta

from data.repopsitory.users_ import UserRepository
import requests
from bs4 import BeautifulSoup


class UpdateUsage:
    def __init__(self):
        self.URL = 'https://www.binance.com/uk-UA/price/bitcoin'

    def access_update_actually(self, user_id):
        if UserRepository()._is_admin_exist(user_id):
            return self.update_actually()

        last_update = UserRepository()._get_last_update(user_id)['last_update']
        if last_update is None or last_update + timedelta(minutes=3) < datetime.now():
            UserRepository()._set_last_update(user_id, datetime.now())
            return self.update_actually()
        else:
            time_to_wait = (datetime.now() - (last_update + timedelta(minutes=3))).strftime('%M:%S')
            return f"can't do update. Wait {time_to_wait} to update"

    def update_actually(self):
        response = requests.get(self.URL)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            tag = soup.find(class_='css-1bwgsh3')
            return tag.text

        return "Some error when do update, try again throw 3 minutes"
