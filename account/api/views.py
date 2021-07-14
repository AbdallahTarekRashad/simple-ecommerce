from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.serializers import UserSerializer, UserLoginDataSerializer, UserLoginSerializer, WishlistSerializer
from account.models import WishList

field_expand = [
    openapi.Parameter('expand', in_=openapi.IN_QUERY,
                      description='Set up fields that be expanded to their fully serialized counterparts via query '
                                  'parameters',
                      type=openapi.TYPE_STRING), ]


class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            return Response(
                data=UserLoginDataSerializer(serializer.save()).data
            )


class UserLoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer
    authentication_classes = ()
    permission_classes = ()

    @swagger_auto_schema(operation_description="You can login with email or username", )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                user = get_user_model().objects.filter(username=username).first()
                if user is not None:
                    user = authenticate(username=user.email, password=password)
            if user is not None:
                if user.is_active:
                    return Response(
                        data=UserLoginDataSerializer(user).data, status=status.HTTP_200_OK
                    )
            raise AuthenticationFailed()


class WishView(APIView):
    serializer_class = WishlistSerializer

    def get_object(self):
        if self.request.user.is_authenticated:
            wish = WishList.objects.get_or_create(customer=self.request.user)[0]
            return wish

    @swagger_auto_schema(operation_id='wish_read', responses={200: WishlistSerializer})
    def get(self, request):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @swagger_auto_schema(operation_id='wish_create', request_body=WishlistSerializer,
                         responses={200: WishlistSerializer})
    def post(self, request):
        wish = self.get_object()
        wish.products.add(*request.data['products'])
        serializer = self.serializer_class(wish)
        return Response(serializer.data)

    @swagger_auto_schema(operation_id='wish_delete', request_body=WishlistSerializer,
                         responses={200: WishlistSerializer})
    def delete(self, request):
        wish = self.get_object()
        wish.products.remove(*request.data['products'])
        serializer = self.serializer_class(wish)
        return Response(serializer.data)


class Me(APIView):
    serializer_class = UserSerializer

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user

    @login_required
    def get(self, request):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)
