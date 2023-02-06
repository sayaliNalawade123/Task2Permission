from rest_framework import APIview 
from .serializers import PostSerializers,PosrModel
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import JWTAuthentication 
from .permission import IsOwnerPermission



from .models import Post

class PostAPIview(APIview):
    serializer_class= PostSerializers
    model_class = PostModel
    permission_classes =[IsOwnerPermission]
    authentication_classes = [JWTAuthentication]


    def get(self,request):
        featched = self.model_class.objects.all()
        serializer = self.serializer_class(featched,many=True)
        return Response(data=serializer.data)


    def post(self,request):
        serializer = self.serializer_class(data=request.data,context={'request':request})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response (data=serializer.errors)

class PostDetailGenericView(RetrieveUpdateDestropyAPIView):
    serializer_class = PostSerializer
    queryset = PosrModel
    Permission_classess = [IsOwnerPermission]
    authentication_classes = [JWTAuthentication]

