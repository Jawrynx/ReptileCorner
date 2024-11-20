from django.urls import path
from . import views

app_name = 'reptiles'

urlpatterns = [
    path('add/', views.add_reptile, name='add_reptile'),
    path('<int:pk>/', views.reptile_detail, name='reptile_detail'),
]