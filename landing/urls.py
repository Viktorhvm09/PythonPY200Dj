from django.urls import path
from .views import LandingView

urlpatterns = [
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
    path('', LandingView.as_view()),
]