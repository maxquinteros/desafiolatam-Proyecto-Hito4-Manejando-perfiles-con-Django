from django.contrib import admin
from django.urls import path, include
from web.views import index, about, welcome, contacto, exito, detalles
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenido/', welcome, name='welcome'),
    path('contacto/', contacto, name='contacto'),
    path('exito/', exito, name='exito'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('detalles/', detalles, name='detalles')
]

