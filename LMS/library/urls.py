from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new_student', views.add_new_student, name='new_student'),
    path('add_new_book', views.add_new_book, name='new_book'),
    path('add_book_issue', views.add_book_issue, name='book_issue'),
    # path('add_new', views.new_add, name='NEW_ST_RECORD'),
    # path('add_new2', views.new2_add, name='NEW_B_RECORD'),
    # path('add_new3', views.new3_add, name='NEW_BI_RECORD'),
    path('show_students', views.view_students, name='SHOW RECORD'),
    path('view_books', views.view_books, name='SHOW BOOK RECORD'),
    path('view_books_issued', views.view_bissue, name='SHOW ISSUED RECORD'),
    path('edit/student/<str:roll>',views.edit_student_data,name="Edit Student data"),

]