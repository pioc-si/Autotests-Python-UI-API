from enums.roles import Roles
from api.api_manager import ApiManager


class Role:
    def __init__(self, role_id, scope="g", href=None):
        if role_id not in Roles.__members__:
            raise ValueError(f"Invalid role:{role_id}")
        self.role_id = role_id
        self.scope = scope
        self.href = href


class User:
    def __init__(self, username: str, password: str, session: ApiManager, roles: list):
        self.username = username
        self.password = password
        self.email = None
        self.roles = roles
        self.groups = None
        self.api_manager = session

    @property
    def creds(self):
        return self.username, self.password

