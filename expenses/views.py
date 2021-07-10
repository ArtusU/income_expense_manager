from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Category, Expense

@login_required(login_url='authentication/login')
def index(request):
    return render(request, 'expenses/index.html')

def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        if not amount:
            messages.error(request, 'Amount is required.')
            return render(request, 'expenses/add_expense.html', context)
        description = request.POST.get('description')
        date = request.POST.get('expense_date')
        category = request.POST.get('category')
        if not description:
            messages.error(request, 'Description is required.')
            return render(request, 'expenses/add_expense.html', context)

        Expense.objects.create(
            amount=amount, 
            description=description, 
            category=category,
            owner=request.user,
            date=date
        )
        messages.success(request, 'Expense saved successfully')

        return redirect('expenses')