from .models import *
from rest_framework import serializers



        
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['name', 'country_id', 'phone_number',
                  'membership_start_date', 'membership_end_date']
        

class BookSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    publications = serializers.PrimaryKeyRelatedField(queryset=Publication.objects.all(), many=True)
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    class Meta:
        model = Book
        fields = ['name', 'written_date',
                  'price_after_delay', 'availability',
                  'categories', 'publications', 'authors']
        

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