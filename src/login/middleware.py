from django.shortcuts import redirect
from django.conf import settings
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        """
        Inicialização do middleware - obrigatório pelo Django
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Lógica executada em cada requisição
        """
        # Lista de URLs que não requerem autenticação
        PUBLIC_URLS = [
            '/login/',
            '/registrer/',
            '/',
            '/index/',
            '/favicon.ico'
        ]
        
        # Verifica se o usuário está autenticado (sua lógica personalizada)
        if not request.session.get('user_id') and request.path not in PUBLIC_URLS:
            return redirect('/login/')
        
        return self.get_response(request)