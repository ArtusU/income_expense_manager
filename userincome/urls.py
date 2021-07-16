from django.urls import path
from .views import index, add_income

urlpatterns = [
    path('', index, name="income"),
    path('add-income', add_income, name="add-income"),
]
