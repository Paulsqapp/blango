from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from blog.api.serializers import PostSerializer
from blog.api.permissions import AuthorModifyOrReadOnly,IsAdminUserForObject
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    #permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer