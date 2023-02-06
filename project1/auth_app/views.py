from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer


class UserAPI(CreateAPIView):
    serializer_class = UserSerializer
    