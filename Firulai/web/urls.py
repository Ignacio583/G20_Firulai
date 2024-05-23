from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Refugio_1', views.Refugio_1, name='Refugio_1'),
    path('FormularioAdop',views.FormularioAdop, name='FormularioAdop')
]
