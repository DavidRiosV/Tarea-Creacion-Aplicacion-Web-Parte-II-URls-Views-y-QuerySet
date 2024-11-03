# urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index_html'),
    path('perfil/<str:alias>', views.listar_perfil, name='listar_perfil'),  #Entrada por string.
    path('coleccion/<int:numero_juegos>/', views.listar_coleccion, name='listar_coleccion'), #Entrada por enteros.
    path('distribuidora/<str:nombre>/<str:pais_origen>/', views.detalle_distribuidora, name='detalle_distribuidora'),  #Entrada múltiple.
    path('amigos/amistad/', views.amigos_amistad, name='amigos_amistad'), #Agregate y filtro agregate.
    path('juegos/', views.listar_juegos, name='listar_juegos'), #Limit y order by.
    path('juegos/comentarios/', views.juegos_sin_comentario, name='juegos_sin_comentario'), #Filtro con None.
    path('usuario/carritos/', views.listar_carritos, name='listar_carritos'), #Uso de related name.
    path('carritos/', views.todos_los_carritos, name='todos_los_carritos'), #URL de relleno, muestra todos los carritos.
    path('bibliotecas/', views.todas_las_bibliotecas, name='todas_las_bibliotecas'), #URL de relleno, muestra todos las bibliotecas.
    path('puntos/', views.todos_los_puntos, name='todos_los_puntos'), #URL de relleno, muestra todos los puntos.
]