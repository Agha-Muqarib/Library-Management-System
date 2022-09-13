from django import forms
from .models import Students, Book, Book_Issue,BookInstance

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
class Book_instanceForm(forms.ModelForm):
    class Meta:
        model=BookInstance
        fields = ['book','book_number']

class Book_IssueForm(forms.ModelForm):
    class Meta:
        model=Book_Issue
        exclude = ['issue_date', 'due_date','remarks_on_return','date_returned']