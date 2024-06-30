from rest_framework import status
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk, user=request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.filter(is_active=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return False

    def get(self, request, pk):
        post = self.get_post(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        comments = post.comments.filter(is_approved=True)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        post = self.get_post(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return False

    def get(self, request, pk):
        post = self.get_post(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        likes = post.likes.filter(is_liked=True).count()
        serializer = LikeSerializer(likes, many=True)
        return Response({'likes': likes})

    def post(self, request, pk):
        post = self.get_post(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








