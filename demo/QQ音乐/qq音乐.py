import requests
import time


def login():
    login_url = 'https://ssl.ptlogin2.qq.com/login'
    params = {
        "u": "123123123",
        "verifycode": "@KgQ",
        "pt_vcode_v1": "1",
        "pt_verifysession_v1": "t03DxMDm5_IJ4-fGSrerio8k6WP6329o_PXs-uI84-D3Y2jTM4aEDelj6KsEG3VZsA6bDHCsl-qlpgfNSjdEa3MviQxranMGTCi77UelnIvKmVJgyy3J7UWYWIhq3Uki-D3",
        "p": "d8hNc79uG*UoOHPKIk0UL8gDpsamAl-CpYRuPyRiIDivM-fbAeCtrVjzrUEVwdxh8zDmqrAGo5limpA4vOnZGjy3lgoleJjdYz2johy8W7WYbzMS8dVP-aZOtc2oACjJnFszES0RbBRAjV*QwEff2dSItXku5KtqpWXlO56D9OTxBbKs1LANnz4VNrKNf8NE6vW9JxliXDNFa23wrxvM3pPlwOBBe61CDu10jruVUsImGMfcBBzTS6GDk9OqiENDOG1LN0JHeDRZcMVrVQ0nk0E*CLZJKcGxmvEdkQPgMBEArpIRXtchdOo1Ixv*ExkDuFXQIRQCWKEPEyky5VShYA__",
        "pt_randsalt": "2",
        "u1": "https://graph.qq.com/oauth2.0/login_jump",
        "ptredirect": "0",
        "h": "1",
        "t": "1",
        "g": "1",
        "from_ui": "1",
        "ptlang": "2052",
        "action": "4-18-1663138197285",
        "js_ver": "22080914",
        "js_type": "1",
        "login_sig": "5zklZFmgFjhc1maO8dciudtRdgImxC8AmdDawO7n4QJF68RlnCM6JbXEMsIm6oQS",
        "pt_uistyle": "40",
        "aid": "716027609",
        "daid": "383",
        "pt_3rd_aid": "100497308",
        "ptdrvs": "4v7kgHWK3-B*CjRYNfDVlXbvh0U5a2ZqPvnh0bOsVIU5YpdOJph*fqC5ZUt7R76iLqtRXJmJbzQ_",
        "sid": "7633867610783840614",
        "": "",
        "o1vId": "8235fa3fa2480570cc054753e5381e98"
    }
    res = session.get(login_url, headers=session.headers, params=params)
    print(res.text)
    ...


def get_song():
    url = 'https://dl.stream.qqmusic.qq.com/C400004Vslx12eRnl8.m4a'
    params = {
        'guid': '1595003526',
        'vkey': 'C213A979F05EDFEBDD021C4832CB5F64C40E46E5938E41936FA0538CDF3D8CFF42D1C61E14F3853417D483460E7BA8E18515A35899A5AFD0',
        'uin': '562172420',
        'fromtag': '120032',
    }


    res = requests.post(url, headers=session.headers, params=params)


def main():
    login()
    ...


if __name__ == '__main__':
    session = requests.session()
    session.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    main()
