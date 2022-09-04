from django.shortcuts import render, redirect
from .forms import StudentsForm, BookForm, Book_IssueForm
from .models import Students, Book, Book_Issue


def index(request):
    return(render(request, 'index.html'))

def add_new_student(request):
    if request.method=="POST":
        form = StudentsForm((request.POST))
        # print(request.POST["fullname"])

        print(form)
        
        if form.is_valid():
            return redirect('/show')

    else:
        form = StudentsForm
    return (render(request, 'add_new_student.html', {'form':form}))

def add_new_book(request):
    form = BookForm
    return (render(request, 'add_new_book.html', {'form':form}))

def add_book_issue(request):
    form = Book_IssueForm
    return (render(request, 'add_book_issue.html', {'form':form}))

def new_add(request):
    # form = StudentsForm(request.POST)
    # form.save()

    stud = Students.objects.order_by('-id')
    return render(request,'view_st.html', {'stud': stud})
    return redirect('/show')

def new2_add(request):
    form = BookForm(request.POST)
    form.save()
    return redirect('/show2')

def new3_add(request):
    form = Book_IssueForm(request.POST)
    form.save()
    return redirect('/show3')

def view_student(request):
    stud = Students.objects.order_by('-id')
    return render(request,'view_st.html', {'stud': stud})

def view_book(request):
    bk = Book.objects.order_by('-id')
    return render(request,'view_b.html', {'bk': bk})

def view_bissue(request):
    issue = Book_Issue.objects.order_by('-id')
    return render(request,'issue_records.html', {'issue': issue})