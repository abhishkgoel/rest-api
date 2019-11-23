from django.urls import path
from .views import list_app, create_app, update_app, delete_app

urlpatterns = [
    path('', list_app, name = 'list_app'),
    path('new', create_app, name='create_app'),
    path('update/<int:id>/', update_app, name='update_app'),
    path('delete/<int:id>/', delete_app, name='delete_app')
]