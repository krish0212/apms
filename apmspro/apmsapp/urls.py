from django.urls import path
from .views import *

#app_name = 'parking'
app_name = "parking"

urlpatterns = [
    path('create/', create_parking_lot, name='create_parking_lot'),
    path('', parking_lots, name='parking_lots'),
    path('<int:id>/', view_parking_lot, name='view_parking_lot'),
]

