from django.urls import path 
from cookBook.views import home, edit, delete

urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:recipe_id>', delete, name='delete'),
    path('edit/<int:recipe_id>', edit, name='edit')
]