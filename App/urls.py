from django.urls import path
from .views import home, addtodo, deletetodoview

urlpatterns = [
    path('', home, name='home'),
    path('addToDoItem/', addtodo),
    path('deletetodoitem/<int:i>/', deletetodoview),
]