# Creacion-Aplicacion-Web-Parte-II-URls-Views-y-QuerySet

## Detalles de las URLs y los requisitos 

### URL 1
- **nombre**: Ver perfil de usuario.
- **funcion**: Obtiene un perfil de usuario a partir del alias proporcionado y muestra la información relacionada.
- **cumple**:
- Un parámetro str.
- Filtros con OR en el HTML.

### URL 2
- **nombre**: Ver colección de un usuario.
- **funcion**: Filtra y muestra las colecciones que tienen un número específico de juegos.
- **cumple**:
- Un parámetro entero.

### URL 3
- **nombre**: Detalles de una distribuidora.
- **funcion**: Obtiene información sobre una distribuidora específica, basada en el nombre y el país de origen.
- **cumple**:
- Dos parámetros.
- Filtros con AND.

### URL 4
- **nombre**: Niveles de amistad.
- **funcion**: Calcula el promedio del nivel de amistad entre los amigos. Luego, filtra aquellos amigos cuyo nivel de amistad es superior a este promedio.
- **cumple**:
- Aggregate.
- Filtro de aggregate.

### URL 5
- **nombre**: Ultimo juego lanzado.
- **funcion**: Obtiene el juego más reciente y lo pasa a la plantilla.
- **cumple**:
- Order_by.
- Limit.

### URL 6
- **nombre**: Juegos sin comentario.
- **funcion**: Esta vista obtiene todos los juegos que no tienen comentarios asociados.
- **cumple**:
- Filtro con None en una tabla intermedia.

### URL 7
- **nombre**: Carritos de cada usuarios.
- **funcion**: Obtenemos todos los carritos y sus usuarios a traves de un related name.
- **cumple**:
- Usando una relación reversa.

### URL 8
- **nombre**: Todos los carritos.
- **funcion**: Mostrar todos los carritos.

### URL 9
- **nombre**: Todas las bibliotecas.
- **funcion**: Mostrar todas las bibliotecas.

### URL 10
- **nombre**: Todas los puntos.
- **funcion**: Mostrar todos los puntos.

### Falta 
- Uso de re_path.

- ### Apuntes
-Los css de mis html son pura decoracion para que se vea todo mas limpio y claro pero no es parte como tal de ningun requisito.





