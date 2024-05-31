from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Refugio_1', views.Refugio_1, name='Refugio_1'),
    path('alta_postulante',views.alta_postulante, name='alta_postulante'),
    path('Contacto',views.Contacto, name='Contacto'),
]
