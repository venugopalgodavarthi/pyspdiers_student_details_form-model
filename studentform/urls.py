from django.urls import path
from studentform import views
urlpatterns=[
    path('form/',views.pyreg,name='form')
]