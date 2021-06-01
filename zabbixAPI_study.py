#!/usr/bin/env python
# coding=utf-8
import requests
import json

# https://qiita.com/Trickey/items/d51d93d525443baa496f

class ZabbixApi(object):
    def __init__(self, uri, user, password):
        """Zabbix API インスタンスを返す

        :param uri: Zabbix サーバの IP アドレス
        :param user: Zabbix API のアクセスユーザ
        :param password: Zabbix API のアクセスユーザパスワード
        :return:
        """
        self.uri = uri
        self.request_id = 1
        self.auth_token = "b3679b287a"
        # self.auth_token = self.post_request('user.login', {'user': user, 'password': password})
        print("auth_token:", self.auth_token)


    def post_request(self, method, params, auth_token=None):
        """Zabbix API にリクエストを送信する
        id は現行特に必要ないため単純にインクリメントした数値を代入している。

        :param method: Zabbix API のメソッド名
        :param params: Zabbix API のメソッドの引数
        :param auth_token: Zabbix API の認証トークン
        :return: JSON-RPC2.0 形式の応答
        """
        if hasattr(self, 'auth_token'):
            auth_token = self.auth_token
        uri = "http://{0}/zabbix/api_jsonrpc.php".format(self.uri)
        headers = {"Content-Type": "application/json-rpc"}
        data = json.dumps({'jsonrpc': '2.0',
                           'method': method,
                           'params': params,
                           'auth': auth_token,
                           'id': self.request_id})
        request = requests.post(uri, data=data, headers=headers)
        print("request_id:",self.request_id)
        self.request_id += 1
        return request.json()["result"]

    def logout(self,auth_token):
        request = requests.post(uri, data=data, headers=headers)
        print("request_id:",self.request_id)


if __name__ == '__main__':
    # Zabbix Server
    api = ZabbixApi('10.246.', 'Admin', 'zabbix')

    # Search Group
    testGroup = "統合WAN"
    params_hostgroupget = {"output": ["groupid","name"]}
    response_hostgroupget = api.post_request('hostgroup.get', params_hostgroupget)
    # print(response_hostgroupget)
    for i in range(len(response_hostgroupget)):
        if testGroup == response_hostgroupget[i]["name"]:
            geted_groupid = response_hostgroupget[i]["groupid"]
            print(testGroup,":",response_hostgroupget[i]["groupid"])

    # Search Host
    params_hostget = {"groupids": geted_groupid, "output": ["hostid","host"], "selectInterfaces": ["interfaceid","ip","type",]}
    response_hostget = api.post_request('host.get', params_hostget)
    geted_hosts = []
    geted_hostsids = []
    myHostIp = ["10.252.216.53"]
    for i in range(len(response_hostget)):
        if response_hostget[i]["interfaces"][0]["ip"] in myHostIp:
            geted_hosts.append(response_hostget[i])
            geted_hostsids.append(response_hostget[i]["hostid"])
    print(geted_hosts)

    # Search Item by HostID
    params_itemget = {"hostids": geted_hostsids, "output": ["itemid","name","params"]}
    response_itemget = api.post_request('item.get', params_itemget)
    for i in range(len(response_itemget)):
        geted_itemids = response_itemget[i]["itemid"]
        print(response_itemget[i])

    # Update Item by Itemid
    params_itemupdate = {"itemid": geted_itemids, "params":"10000"}
    response_itemget = api.post_request('item.update', params_itemupdate)
    print(response_itemget)




    # user.logout



    # if 'result' in response:
    #     # 成功時の処理

    # elif 'error' in response:
    #     pass # 失敗時の処理
    # else:
    #     pass # 不具合時の処理
