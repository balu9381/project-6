from django.urls import path
from app2.views import *
app_name='bala'

urlpatterns=[
    path('ravi/',ravi,name='ravi'),
    path('teja/',teja,name='teja'),
]