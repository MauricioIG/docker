from rest_framework import serializaers
from .models import Post

class PostSerializer(serializaers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'titulo', 'contenido', 'autor', 'fecha_publicacion']
        
