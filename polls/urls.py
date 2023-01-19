from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/', views.UserList.as_view()),
    path('pdf/<int:pk>/', views.Userupdate.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
