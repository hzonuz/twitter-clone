from django.contrib.auth.password_validation import validate_password
from rest_framework.views import APIView, status
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        password = request.data.get("password")
        serializer = self.get_serializer(data=request.data)
        validate_password(password, user=request.user)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance
        user.set_password(password)
        user.save()

        token = Token.objects.create(user=user)
        result_data = serializer.data
        result_data['token'] = token.key

        return Response(result_data, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    # queryset = User.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return User.objects.get(id=self.kwargs.get("user_pk"))

