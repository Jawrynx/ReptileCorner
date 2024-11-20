from django.urls import path
from . import views

app_name = 'reptiles'

urlpatterns = [
    path('add/', views.add_reptile, name='add_reptile'),
    path('<int:pk>/', views.reptile_detail, name='reptile_detail'),
    path('<int:pk>/edit/', views.edit_reptile, name='edit_reptile'),
    path('list/', views.reptiles_list, name='reptiles_list'),
]