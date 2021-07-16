from django.urls import path
from .views import index, add_income, income_edit, delete_income

urlpatterns = [
    path('', index, name="income"),
    path('add-income', add_income, name="add-income"),
    path('edit-income/<int:id>', income_edit, name="income-edit"),
    path('income-delete/<int:id>', delete_income, name="income-delete"),
]
