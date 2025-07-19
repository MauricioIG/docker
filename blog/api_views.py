from rest_framework import generics
from .model import Post
from .serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdatedestroyAPIWiew):
    queryst = Post.objests.all()
    serializser_class = PostSerializer
    