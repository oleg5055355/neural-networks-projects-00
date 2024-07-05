from django.apps import AppConfig


class NewsAppConfig(AppConfig):
    name = 'news_app'

    def ready(self):
        import news_app.signals
