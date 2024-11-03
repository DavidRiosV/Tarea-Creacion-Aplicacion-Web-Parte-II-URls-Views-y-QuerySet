from django.shortcuts import render
from django.db.models import Q,Prefetch
from django.db.models import Avg
from .models import Usuario,Carrito,Biblioteca,Puntos,Distribuidora,Juego,Perfil,Tienda,Amigos,Coleccion,ColeccionBibliotecaJuego
from django.shortcuts import render
from django.views.defaults import page_not_found


# Menu donde estan mis url
def index(request):
    return render(request,'index.html') 

# Obtiene un perfil de usuario a partir del alias proporcionado y muestra la información relacionada.
def listar_perfil(request, alias):
    perfil = Perfil.objects.select_related('usuario').filter(alias = alias)
    return render(request, 'listar_perfil.html', {'perfil': perfil})

# Filtra y muestra las colecciones que tienen un número específico de juegos 
def listar_coleccion(request, numero_juegos):
    coleccion = Coleccion.objects.filter(numero_juegos = numero_juegos)
    return render(request, 'listar_coleccion.html', {'coleccion': coleccion})

# Obtiene información sobre una distribuidora específica, basada en el nombre y el país de origen
def detalle_distribuidora(request, nombre, pais_origen):
    distribuidora = Distribuidora.objects.filter(Q(nombre = nombre) & Q(pais_origen = pais_origen)).all()
    return render(request, 'detalle_distribuidora.html', {'distribuidora': distribuidora })
    
# Calcula el promedio del nivel de amistad entre los amigos. Luego, filtra aquellos amigos cuyo nivel de amistad es superior a este promedio.
def amigos_amistad(request):
    amistad = Amigos.objects.aggregate(Avg('nivel_amistad'))
    media = amistad['nivel_amistad__avg']
    amigos_filtrados = Amigos.objects.filter(nivel_amistad__gt=media)
    return render(request, 'amigos_amistad.html', {'amistad': amistad, 'media': media, 'amigos_filtrados': amigos_filtrados})

# Obtiene el juego más reciente y lo pasa a la plantilla.
def listar_juegos(request):
    juegos_recientes = Juego.objects.order_by('-fecha_lanzamiento')[:1]
    return render(request, 'listar_juegos.html', {'juegos_recientes': juegos_recientes })

# Esta vista obtiene todos los juegos que no tienen comentarios asociados.
def juegos_sin_comentario(request):
    juegos = ColeccionBibliotecaJuego.objects.select_related("coleccion", "biblioteca", "juego")
    juegos = juegos.filter(comentario=None)
    return render(request, 'juegos_sin_comentario.html', {"juegos_mostrar": juegos})

# Obtenemos todos los carritos y sus usuarios a traves de un related name
def listar_carritos(request):
    usuarios = Usuario.objects.select_related('user').all()
    return render(request, 'listar_carritos.html', {'usuarios': usuarios})

# Mostrar todos los carritos
def todos_los_carritos(request):
    carrito = Carrito.objects.all()
    return render(request, 'todos_los_carritos.html', {'carrito': carrito})

# Mostrar todas las bibliotecas
def todas_las_bibliotecas(request):
    biblioteca = Biblioteca.objects.all()
    return render(request, 'todas_las_bibliotecas.html', {'biblioteca': biblioteca})

# Mostrar todos los puntos
def todos_los_puntos(request):
    puntos = Puntos.objects.all()
    return render(request, 'todos_los_puntos.html', {'puntos': puntos})

# Páginas de Error
def mi_error_400(request,exception=None):
    return render(request, 'errores/400.html',None,None,400)

def mi_error_403(request,exception=None):
    return render(request, 'errores/403.html',None,None,403)

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)