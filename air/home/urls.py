from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='Home'),
    path('aboutus/', Aboutus, name='Aboutus'),
    path('bookticket/', bookticket1, name='bookticket1'),

]

