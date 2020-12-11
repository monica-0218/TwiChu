from django.urls import path
from .views import TopView, AdaptionView, HomeView, PostListView, PostDetailView, PostUpdateView, UserSettingView

app_name = 'chusen'
urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('home/', HomeView.as_view(), name='home'),
    path('post/', PostListView.as_view(), name='postlist'),
    path('post/<int:pk>', PostDetailView.as_view(), name='postdetail'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='postupdate'),
    path('user/<int:pk>', UserSettingView.as_view(), name='usersetting'),
    path('user/postupdate/<int:pk>', PostUpdateView.as_view(), name='postupdate'),
    path('adaption/', AdaptionView.as_view()),
]
