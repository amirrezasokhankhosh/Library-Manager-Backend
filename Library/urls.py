from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'members', MemberViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
router.register(r'borrows', BorrowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
