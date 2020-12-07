from django.urls import path
from .views import TopView, AdaptionView, HomeView

app_name = 'chusen'
urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('home/', HomeView.as_view()),
    path('adaption/', AdaptionView.as_view()),
]
