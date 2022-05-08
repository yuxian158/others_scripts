import json
import os
import requests


class ql():
    def __init__(self, url, post, client_id, client_secret, env_name):
        self.url = f"http://{url}:{post}"
        self.client_id = client_id
        self.client_secret = client_secret
        self.s = requests.session()
        self._get_qltoken()
        self.env_name = env_name

    def _get_qltoken(self):
        url = f"{self.url}/open/auth/token?client_id={self.client_id}&client_secret={self.client_secret}"
        res = self.s.get(url)
        token = json.loads(res.text)["data"]['token']
        self.s.headers.update({"authorization": "Bearer " + str(token)})
        self.s.headers.update({"Content-Type": "application/json;charset=UTF-8"})

    def get_env(self):
        url = f"{self.url}/open/envs?searchValue={self.env_name}"
        res = self.s.get(url=url).json().get("data")
        id_list = []
        for i in res:
            print(i.get('id'), i.get('value'))
            id_list.append(i.get('id'))
        return id_list

    def del_env(self):
        id_list = self.get_env()
        url = f"{self.url}/open/envs"
        for id in id_list:
            data = f"{[id]}"
            print(self.s.delete(url=url, data=data))
            print(f"删除{id}成功")

    def add_env(self):
        new_env = os.environ.get(self.env_name)
        new_env_list = new_env.split("&")
        url = f"{self.url}/open/envs"
        for i in new_env_list:
            data = [{"value": i, "name": self.env_name}]
            data = json.dumps(data)
            print(self.s.post(url=url, data=data))

    def change_env(self):
        new_env = os.environ.get(self.env_name)
        new_env_list = new_env.split("&")
        url = f"{self.url}/open/envs"
        id_list = self.get_env()
        for x, y in zip(new_env_list, id_list):
            data = {
                "value": x,
                "name": self.env_name,
                "remarks": "",
                "id": y
            }
            data=json.dumps(data)
            print(f"将id={y}改为{x}")
            self.s.put(url=url, data=data)


ql = ql(url=os.environ.get("ql_url"),
        post=os.environ.get("ql_post"),
        client_id=os.environ.get("client_id"),
        client_secret=os.environ.get("client_secret"),
        env_name="JD_COOKIE")
ql.change_env()
