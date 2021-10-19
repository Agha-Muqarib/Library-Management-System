from django.shortcuts import render, redirect
from .forms import StudentsForm, BookForm, Book_IssueForm
from .models import Students, Book, Book_Issue


def index(request):
    return(render(request, 'index.html'))

def new_form(request):
    form = StudentsForm
    return (render(request, 'new_form.html', {'form':form}))

def new2_form(request):
    form = BookForm
    return (render(request, 'new2_form.html', {'form':form}))

def new3_form(request):
    form = Book_IssueForm
    return (render(request, 'new3_form.html', {'form':form}))

def new_add(request):
    form = StudentsForm(request.POST)
    form.save()
    return redirect('/show')
def new2_add(request):
    form = BookForm(request.POST)
    form.save()
    return redirect('/show2')
def new3_add(request):
    form = Book_IssueForm(request.POST)
    form.save()
    return redirect('/show3')

def view_st(request):
    stud = Students.objects.order_by('-id')
    return render(request,'view_st.html', {'stud': stud})

def view_b(request):
    bk = Book.objects.order_by('-id')
    return render(request,'view_b.html', {'bk': bk})

def view_bissue(request):
    issue = Book_Issue.objects.order_by('-id')
    return render(request,'view_bissue.html', {'issue': issue})