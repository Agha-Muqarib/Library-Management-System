from django.db import models
from datetime import datetime,timedelta

class Students(models.Model):
    roll_number = models.CharField(max_length=100,unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    Guardian_name=models.CharField(max_length=100,help_text="parent/guardian full name")
    Email=models.EmailField(max_length=100,help_text="Guardian/parent e-mail")
    def __str__(self):
        return self.std_name
    def __str__(self):
        return str(self.std_rn)

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_pages = models.IntegerField()
    summary=models.TextField(max_length=500, help_text="Summary about the book",null=True,blank=True)
    def __str__(self):
        return self.book_title


def get_returndate():
    return datetime.today() + timedelta(days=8)

class Book_Issue(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(default=get_returndate())
    remarks = models.CharField(max_length=100, default="Some Remarks")
    returned=models.BooleanField(default=True)
    borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.Students.std_name + " borrowed " + self.Book.book_title