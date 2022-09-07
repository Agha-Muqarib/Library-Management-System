from secrets import choice
from django.shortcuts import render, redirect,HttpResponse
from .forms import StudentsForm, BookForm, Book_IssueForm
from .models import Students, Book, Book_Issue
# from random 
import random


def index(request):
    return(render(request, 'index.html'))


def add_new_student(request):
    if request.method=="POST":
        form = StudentsForm((request.POST))
        if form.is_valid():
            # save data
            form.save()
            return redirect('/show_students')
    else:
        form = StudentsForm
    return (render(request, 'add_new_student.html', {'form':form}))


def add_new_book(request):
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            # save data
            form.save()
            return redirect('/view_books')
    else:
        form = BookForm
        return (render(request, 'add_new_book.html', {'form':form}))


def add_book_issue(request):
    if request.method=="POST":
        form = Book_IssueForm(request.POST)
        if form.is_valid():
            # save data
            form.save()
            return redirect('/view_books_issued')
    else:
        form = Book_IssueForm
        return (render(request, 'add_book_issue.html', {'form':form}))

def view_students(request):
    students = Students.objects.order_by('-id')
    return render(request,'view_students.html', {'students': students})

def view_books(request):
    books = Book.objects.order_by('-id')
    return render(request,'view_books.html', {'books': books})

def view_bissue(request):
    issue = Book_Issue.objects.order_by('-id')
    return render(request,'issue_records.html', {'issue': issue})

def save_edited_data(id,data_dict):
    pass

def edit_student_data(request,roll):
    try:
        student_id=""
        if request.method == "POST":
            std_roll=request.POST.get("roll_number")
            std_name=request.POST.get("student_name")
            std_program=request.POST.get("program")
            std_address=request.POST.get("address")
            std_guardian=request.POST.get("Guardian_name")
            email=request.POST.get("email")
            message=f"{std_name} edited"

            # return render(request, 'index.html', {'message':message})
            return redirect("/show_students",message)
        else:
            student=Students.objects.filter(roll_number=roll).values()[0]
            student_id=student["id"]
            return render(request,'edit_student_data.html',{'student':student})


    except Exception as error:
        print(f"{error} occured at edit_student_data view")

def delete_student(request,roll):
    return HttpResponse("<h2>The feature is comming soon</h2>")
    pass

def delete_book(request,id):
    return HttpResponse("<h2>The feature is comming soon</h2>")
    pass