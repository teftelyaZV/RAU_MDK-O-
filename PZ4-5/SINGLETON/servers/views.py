from django.http import HttpResponse

from servers.singleton import AccessManager

from servers.models import AccessRequestFactory


def index(request):
    try:
        manager = AccessManager()
        manager.register_request("read")
        manager.register_request("write")

        read_req = AccessRequestFactory.create_request("read", "user123", "table_users")
        
        html = f"""
        
        <h1>Система управления доступом к БД (DAM)</h1>
        
        <p>Singleton ID: {id(manager)}</p>
        
        <p>Зарегистрированные запросы: {manager.get_all_requests()}</p>
        
        <p>Пример Factory: {read_req.get_info()}</p>
        
        """
    except Exception as error:
        html = f"<h1>Ошибка:</h1><p>{error}</p>"

    return HttpResponse(html)