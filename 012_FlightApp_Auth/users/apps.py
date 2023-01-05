from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
# signal işlemlerini model'de değil de ayrı bir dosyada oluşturduğum için apps.py'ye aşağıdaki kodu ekliyorum.
    def ready(self) -> None:
        import users.signals
