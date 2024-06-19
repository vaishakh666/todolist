from django.urls import path
from  . import views
urlpatterns = [
    path('',views.home),
    path('home',views.home,name='home'),
    path('todo',views.todo,name="todo"),
    path('del/<int:id>',views.delete,name="delete"),
    path('edit/<int:id>',views.edit,name="edit"),
]
