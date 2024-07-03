from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import  *

urlpatterns = [
    path('', views.index, name="index"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="web/registration/login.html"), name="login"),
    path("accounts/logout/", views.user_logout, name="logout"),
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="web/registration/password_reset.html"), name="password_reset"),
    #path("accounts/login/", auth_views.LoginView.as_view(template_name="web/registration/login.html"), name="login"),    
    path('refugio', views.refugio, name='refugio'),
    path('alta_mascota',views.alta_mascota, name='alta_mascota'),
    path('alta_postulante',views.alta_postulante, name='alta_postulante'),
    path('alta_adopcion', views.alta_adopcion, name='alta_adopcion'),
    path('listado_adopciones', views.AdopcionesLista.as_view(), name='listado_adopciones'),
    path('listado_postulante', views.PostulanteListView.as_view(), name='listado_postulante'),
    path('listado_colaborador', views.ColaboradorListView.as_view(), name='listado_colaborador'),
    
]
#web/listado_adopciones.html