from rest_framework.views import APIView
from school_api.serializers import *
from schoolApp.models import *
from rest_framework import status
from rest_framework import mixins,generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# Teacher Views
class ClasssAPI(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAdminUser]
    queryset = Classs.objects.all()
    serializer_class = ClasssSerializer

    def get(self,request,pk):
        return self.retrieve(request)

    def patch(self,request,pk):
        return self.update(request, partial=True)
    
    def delete(self,request,pk):
        return self.destroy(request)

   
class ClasssListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAdminUser]
    queryset = Classs.objects.all()
    serializer_class = ClasssSerializer

    def post(self,request):
        return self.create(request)
    
    def get(self, request):
        return self.list(request)
   
   
   
   
    # def get(self,request,id=None,format=None):
    #     id = id
    #     if id is not None:
    #         classes = Classs.objects.get(id = id)
    #         serializer = ClasssSerializer(classes)
    #         return Response(serializer.data)

    #     classs = Classs.objects.all()
    #     serializer = ClasssSerializer(classs,many = True)
    #     return Response(serializer.data)


    # def post(self,request,format=None):
    #     serializer = ClasssSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def patch(self, request, id, fromat=None):
    #     id = id
    #     classs = Classs.objects.get(id=id)
    #     serializer= ClasssSerializer(classs,data = request.data, partial= True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Partial Data Updated'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, id, format=None):
    #     id = id
    #     classs = Classs.objects.get(id= id)
    #     classs.delete()
    #     return Response({'msg':'Data Deleted Successfully'})