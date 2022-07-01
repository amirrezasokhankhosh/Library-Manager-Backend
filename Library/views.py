from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from .permissions import IsAdmin
from django.contrib.auth import get_user_model


UserModel = get_user_model()
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny, IsAdmin]
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny, IsAdmin]
    
    
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.AllowAny, IsAdmin]
    
class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.AllowAny, IsAdmin]
    

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny, IsAdmin]

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, IsAdmin]
    
    
class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.AllowAny, IsAdmin]
