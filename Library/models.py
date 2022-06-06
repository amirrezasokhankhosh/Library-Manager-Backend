from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    
    name = models.CharField(max_length=200, unique=True, null=False)
    

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Category(models.Model):
    
    name = models.CharField(max_length=200, unique=True, null=False)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Member(models.Model):

    name = models.CharField(max_length=200, null=False)
    country_id = models.CharField(max_length=100, unique=True, null=False)
    phone_number = models.CharField(
        max_length=11, null=False, default='9111111111')
    date_added = models.DateTimeField(auto_now_add=True)
    membership_start_date = models.DateField()
    membership_end_date = models.DateField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Publication(models.Model):

    name = models.CharField(max_length=200, unique=True, null=False)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
    
    
class Book(models.Model):
    name = models.CharField(max_length=200, null=False)
    written_date = models.DateField()
    price_after_delay = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    availability = models.BooleanField()
    
    
    publications = models.ManyToManyField(Publication, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')
    authors = models.ManyToManyField(Author, related_name='books')
    
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.name

    class Meta:
        unique_together = ('name', 'written_date')
        
        
class Borrow(models.Model):
    
    book_id = models.ForeignKey(Book, related_name='borrows', on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, related_name='borrows', on_delete=models.CASCADE)
    duration_days = models.IntegerField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateField(null=True, blank=True)
    total_delay_fee = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.member_id) + " for " + str(self.duration_days) + " days of book " + str(self.book_id)

    class Meta:
        unique_together = ('book_id', 'member_id', 'date_added')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.BooleanField(null=False)
    