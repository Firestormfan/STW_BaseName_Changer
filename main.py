# Thanks for EpicResearch(https://github.com/MixV2/EpicResearch)

import requests

FN_AUTH_BASE = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
FN_AUTHORIZATION = "https://www.epicgames.com/id/api/redirect?clientId=3446cd72694c4a4485d81b77adbb2141&responseType=code"
FN_BASIC = "basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="
FN_HB_URL = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{}/client/SetHomebaseName?profileId=common_public&rvn=-1"

hb_name = input("新しい拠点名を入力してください: ")
code = input("{} にアクセスし、fnauth?code=の後をコピーし、貼り付けてください: ".format(FN_AUTHORIZATION))

a_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": FN_BASIC
}
a_body = {
    "grant_type": "authorization_code",
    "code": code
}

data = requests.post(FN_AUTH_BASE, headers=a_headers, data=a_body).json()
token = data.get("access_token", None)
if token is None:
    print("認証に失敗しました。")
    exit()
else:
    m_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token)
    }
    m_json = {
        "homebaseName": hb_name
    }
    x = requests.post(
        FN_HB_URL.format(data["account_id"]),
        headers=m_headers,
        json=m_json
    ).json()
    if x.get("profileId") == "common_public":
        print("拠点名を変更しました。")
    else:
        print("拠点名の変更に失敗しました。")