from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from user.serializer import SignUpSerializer
from django.contrib.auth.hashers import check_password
from user.models import UserModel
# Create your views here.



class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        if not username or password:
            return Response({"message":"아이디와 비밀번호를 입력해 주세요."}, status=status.HTTP_400_BAD_REQUEST)

        else:
            user = get_object_or_404(UserModel, username=username)
            if check_password(password, user.password):
                return Response({"message":"로그인 되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message":"아이디와 비밀번호를 확인해 주세요."}, status=status.HTTP_400_BAD_REQUEST)

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"가입이 완료되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message":"가입에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)
