from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model


UserModel = get_user_model()
        
        
class BorrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Borrow
        fields = ['book_id', 'member_id', 'duration_days',
                  'date_ended', 'total_delay_fee']
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    borrows = BorrowSerializer(read_only=True, many=True)
    class Meta:
        model = Member
        fields = ['name', 'country_id', 'phone_number',
                  'membership_start_date', 'membership_end_date',
                  'borrows']
        

class BookSerializer(serializers.HyperlinkedModelSerializer):
    borrows = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    publications = serializers.PrimaryKeyRelatedField(queryset=Publication.objects.all(), many=True)
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    class Meta:
        model = Book
        fields = ['name', 'written_date',
                  'price_after_delay', 'availability',
                  'categories', 'publications', 'authors',
                  'borrows']
        

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = ['name', 'books']

        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ['name', 'books']
        
        
class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Publication
        fields = ['name', 'books']
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user
    
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'password']
        
