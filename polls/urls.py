from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/update', views.update, name='update'),
]
