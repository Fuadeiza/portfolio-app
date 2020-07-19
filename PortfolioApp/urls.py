from django.urls import path, include
from .views import UserPortfolioUpdateView, UserListView, UserDetailView

app_name='PortfolioApp'

urlpatterns = [
    path('update/', UserPortfolioUpdateView.as_view(), name='update'),
    path('list/', UserListView.as_view(), name='list'),
    path('<slug:slug>/', UserDetailView.as_view(), name='detail'), 
]