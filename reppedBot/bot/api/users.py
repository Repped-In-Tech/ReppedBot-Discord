import requests

def remove_member_from_db(member_id, url):
    return requests.request(method='GET', url=url, params={"member_id": member_id}, timeout=3)
