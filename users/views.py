from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UserSerializer


class UsersListApiView(APIView):

    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'password': request.data.get('password')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetailApiView(APIView):

    def get(self, request, user_id):
        user = Users.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        user_instance = Users.objects.get(id=user_id)
        if not user_instance:
            return Response({"message": "user does not exists"},
                            status=status.HTTP_400_BAD_REQUEST)
        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'password': request.data.get('password')
        }
        serializer = UserSerializer(instance=user_instance,
                                    data=data,
                                    partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user_instance = Users.objects.get(id=user_id)
        if not user_instance:
            return Response({"message": "user does not exists"},
                            status=status.HTTP_400_BAD_REQUEST)
        user_instance.delete()
        return Response({"message": "user deleted!"}, status=status.HTTP_200_OK)
