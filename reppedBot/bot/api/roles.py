import requests

def update_user_roles_in_db(member_id, roles, endpoint):
    data = {
      "member_id": member_id[0],
      "roles": [role.id for role in roles]
    }
    return requests.request('POST', endpoint, data=data, timeout=3)
