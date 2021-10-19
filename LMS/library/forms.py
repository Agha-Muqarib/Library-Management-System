from django import forms
from .models import Students, Book, Book_Issue

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class Book_IssueForm(forms.ModelForm):
    class Meta:
        model=Book_Issue
        exclude = ['issue_date', 'return_date']