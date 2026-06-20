from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/',views.categoryi,name='categories'),
    path('categories/add-category',views.add_category,name='add_category'),
    path('categories/edit-category/<int:id>',views.edit_category,name='edit_category'),
    path('categories/delete-category/<int:id>',views.delete_category,name='delete_category'),
    path('posts',views.posts,name='posts'),
    path('posts/add-post',views.add_post,name='add_post'),
    path('posts/edit-post/<int:id>',views.edit_post,name='edit_post'),
    path('posts/delete-post/<int:id>',views.delete_post,name='delete_post'),
    ]