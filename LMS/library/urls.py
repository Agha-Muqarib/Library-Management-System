from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_form', views.new_form, name='new_form'),
    path('new2_form', views.new2_form, name='new2_form'),
    path('new3_form', views.new3_form, name='new3_form'),
    path('add_new', views.new_add, name='NEW_ST_RECORD'),
    path('add_new2', views.new2_add, name='NEW_B_RECORD'),
    path('add_new3', views.new3_add, name='NEW_BI_RECORD'),
    path('show', views.view_st, name='SHOW RECORD'),
    path('show2', views.view_b, name='SHOW BOOK RECORD'),
    path('show3', views.view_bissue, name='SHOW ISSUED RECORD'),
]