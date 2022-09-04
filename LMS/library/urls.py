from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new_student', views.add_new_student, name='new_student'),
    path('add_new_book', views.add_new_book, name='new_book'),
    path('add_book_issue', views.add_book_issue, name='book_issue'),
    path('add_new', views.new_add, name='NEW_ST_RECORD'),
    path('add_new2', views.new2_add, name='NEW_B_RECORD'),
    path('add_new3', views.new3_add, name='NEW_BI_RECORD'),
    path('show', views.view_student, name='SHOW RECORD'),
    path('show2', views.view_book, name='SHOW BOOK RECORD'),
    path('show3', views.view_bissue, name='SHOW ISSUED RECORD'),
]