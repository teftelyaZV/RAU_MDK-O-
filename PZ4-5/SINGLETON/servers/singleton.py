class AccessManager:
    """Singleton: управляет единым реестром запросов на доступ к БД."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.requests = {}
        return cls._instance
        
    def register_request(self, request_type: str) -> str:
        if request_type not in self.requests:
            self.requests[request_type] = f"Зарегистрирован доступ типа {request_type}"
        return self.requests[request_type]
        
    def get_all_requests(self) -> dict:
        return self.requests