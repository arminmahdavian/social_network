from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerializer


# Create your views here.


User = get_user_model()

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        receiver_username = self.request.data.get('receiver')
        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save(sender=self.request.user, receiver=receiver)
        return Response(serializer.data, status=status.HTTP_201_CREATED)











