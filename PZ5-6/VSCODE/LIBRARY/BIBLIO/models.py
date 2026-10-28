from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150)
    birth_year = models.IntegerField(null=True, blank=True)
    citizenship = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_year = models.IntegerField()
    isbn = models.CharField(max_length=20, unique=True)
    genre = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

class Reader(models.Model):
    full_name = models.CharField(max_length=200)
    ticket_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)