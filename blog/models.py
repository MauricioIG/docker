from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comentario de {self.autor} en {self.post.titulo}'


# tipos de campos adicionales los mas populares usados
'''
BooleanField = Booleanos
IntegerField = Numeros enteros
EmailField = Email o correo valido

ForeKey = relacion muchos a muchos
ManyToManyField = relacion a muchos 
'''

# obligatorio despues de manipular los modelos
# hacer las migraciones
'''
python manage.py makemigrationes = crea las migraciones
python manage.py migrate = crea las migraciones

'''
# ORM
