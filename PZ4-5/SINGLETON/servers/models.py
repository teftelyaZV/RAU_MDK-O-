from django.db import models

class AccessRequest:
    def __init__(self, user_name: str, resource: str):
        self.user_name = user_name
        self.resource = resource

    def get_info(self) -> str:
        raise NotImplementedError()


class ReadAccessRequest(AccessRequest):
    def get_info(self) -> str:
        return f"READ: Пользователь {self.user_name} запрашивает доступ к {self.resource}"


class WriteAccessRequest(AccessRequest):
    def get_info(self) -> str:
        return f"WRITE: Пользователь {self.user_name} запрашивает доступ к {self.resource}"


class AdminAccessRequest(AccessRequest):
    def get_info(self) -> str:
        return f"ADMIN: Пользователь {self.user_name} запрашивает доступ к {self.resource}"


class AccessRequestFactory:
    _registry = {
        "read": ReadAccessRequest,
        "write": WriteAccessRequest,
        "admin": AdminAccessRequest,
    }

    @classmethod
    def create_request(cls, request_type, user_name, resource):
        if request_type not in cls._registry:
            raise ValueError(f"Неизвестный тип доступа: {request_type}")
        return cls._registry[request_type](user_name, resource)