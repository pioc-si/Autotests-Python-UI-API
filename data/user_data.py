from enums.roles import Roles
from utils.datagenerator import DataGenerator


class UserData:
    @staticmethod
    def create_user_data(role=Roles.SYSTEM_ADMIN.value, scope="g"):
        return {
            "username": DataGenerator.fake_name(),
            "password": DataGenerator.fake_project_id(),
            "email": "example@mail.com",
            "roles": {
                "role": [
                    {
                        "roleId": role,
                        "scope": scope,
                    }
                ]
            }
        }