from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path('auth/', include('auth.urls')),
    path('perfil/', include('perfil.urls')),
    path('cabecera/', include('cabecera.urls')),
=======
    path('', include('home.urls')),
    path('', include('auth.urls')),
    path('', include('perfil.urls')),
    path('', include('chat.urls')),
    path('', include('upload_image.urls')),
>>>>>>> 6a4eac1e576acbd4060f31f7ccfcb012a4cfa4ad
]
