from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

class GetUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer

class RegisterView(APIView):
    def post(self, request):
        users = request.data
        serializer = RegisterSerializer(data=users)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message":"user logout"},status=status.HTTP_204_NO_CONTENT)