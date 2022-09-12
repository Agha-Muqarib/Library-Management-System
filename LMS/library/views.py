from django.shortcuts import render, redirect,HttpResponse
from .forms import StudentsForm, BookForm, Book_IssueForm,Book_instanceForm
from .models import Students, Book, Book_Issue,BookInstance


def index(request):
    return(render(request, 'index.html'))


def add_new_student(request):
    if request.method=="POST":
        form = StudentsForm((request.POST))
        if form.is_valid():
            form.save()
            return redirect('/show_students')
    else:
        form = StudentsForm
    return (render(request, 'add_new_student.html', {'form':form}))


def add_new_book(request):
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form=form.save()
            book_instance=BookInstance(book=form)
            book_instance.save()
            return redirect('/view_books')
    else:
        form = BookForm
        form_instance=Book_instanceForm
        return (render(request, 'add_new_book.html', {'form':form,"form_instance":form_instance}))

def add_new_book_instance(request):
    form=Book_instanceForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/view_books')


def add_book_issue(request):
    if request.method=="POST":
        form = Book_IssueForm(request.POST)
        if form.is_valid():
            # save data
            unsaved_form=form.save(commit=False)
            book_to_save=BookInstance.objects.get(id=unsaved_form.book_instance.id)
            book_to_save.Is_borrowed=True
            book_to_save.save()
            form.save()
            form.save_m2m()
        return redirect('/view_books_issued')
    else:
        context={'form':Book_IssueForm,"book":BookInstance.objects.filter(Is_borrowed=False)}
        return render(request, 'add_book_issue.html',context=context)

def view_students(request):
    students = Students.objects.order_by('-id')
    return render(request,'view_students.html', {'students': students})

def view_books(request):
    books=BookInstance.objects.order_by('id')
    return render(request,'view_books.html', {'books': books})

def view_bissue(request):
    issue = Book_Issue.objects.order_by('-id')
    return render(request,'issue_records.html', {'issue': issue})


def edit_student_data(request,roll):
    try:
        if request.method == "POST":
            std=Students.objects.get(id=request.session['id'])    
            form = StudentsForm((request.POST),instance=std)
            if form.is_valid():
                form.save()
            del request.session['id']
            return redirect("/show_students")
        else:
            student_to_edit=Students.objects.get(roll_number=roll)
            student=StudentsForm(instance=student_to_edit)
            request.session["id"]=student_to_edit.id
            return render(request,'edit_student_data.html',{'student':student})
    except Exception as error:
        print(f"{error} occured at edit_student_data view")

def edit_book_data(request,id):
    return HttpResponse(f"<label>A book with ID: {id} could not be edited...</label><h2>The feature is comming soon</h2>")

def delete_student(request,roll):
    return HttpResponse(f"<h2>Delete Student</h2><label>Student with Roll Number: {roll} could not be deleted...</label><h2>The feature is comming soon</h2>")
    pass

def delete_book(request,id):
    return HttpResponse(f"<h2>Delete Book</h2><label>Book with ID: {id} could not be deleted..</label><h2>The feature is comming soon</h2>")

def return_issued_book(request,id):   
    obj=Book_Issue.objects.get(id=id)
    return HttpResponse(f"<h2>Return Issued Book</h2><label>Book <i>{obj.book_instance.book.book_title}</i> issued to <i>{obj.student.fullname}</i> could not be returned..</label><h2>The feature is comming soon</h2>")

def edit_issued(request, id):
    obj=Book_Issue.objects.get(id=id)
    return HttpResponse(f"<h2>Edit Issued Book</h2><label>Book <i>{obj.book_instance.book.book_title}</i> issued to <i>{obj.student.fullname}</i> could not be edited..</label><h2>The feature is comming soon</h2>")
