from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
import datetime

# Creating an end point
def search_expenses(request):
    if request.method== 'POST':
       

        search_str = json.load(request.body).get('searchText')
         
        expenses =Expense.objects.filter(
            amount__str_with=search_str, owner=request.user) | Expense.objects.filter(
            date__str_with=search_str, owner=request.user)  | Expense.objects.filter(
            category__icontaisn=search_str, owner=request.user) | Expense.objects.filter(
            description__icontains=search_str, owner=request.user) 
        data = expenses.values()

        return JsonResponse(list(data), safe=False)




# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    categories =Category.objects.all()
    expenses=Expense.objects.filter(owner=request.user)
    paginator=Paginator(expenses, 5) # show 5 objects per page
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator, page_number)
    user= request.user
    context={
            'expenses': expenses,
            'page_obj': page_obj,
            'username': user.username
        }
    return render(request, '_dashboard/index.html', context )


#Updating the records  
@login_required(login_url='/accounts/login')
def add_expenses(request):
    expenses=Expense.objects.filter(owner=request.user)
    categories = Category.objects.all()
    context= { 
        'expenses' : expenses,
        'categories': categories,
        'values': request.POST
        
    } 
    if request.method== 'GET':
        return render(request, '_dashboard/add_expenses.html', context)

    # To check if  fields are empty and display a message if empty
    if request.method== 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, '_dashboard/add_expenses.html', context)
    

        
        description = request.POST['description']
        date = request.POST['date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'Description is required')
            return render(request, '_dashboard/add_expenses.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, '_dashboard/add_expenses.html', context)
        
        # Pushing the records in the database
        Expense.objects.create(owner=request.user,amount=amount, date=date, category=category, description=description)

        messages.success(request, 'Expense saved successfully')

        return redirect( 'dashboard:dashboard')
     

@login_required(login_url='/accounts/login')    
def expense_edit(request, id):
    expense =Expense.objects.get(pk=id)
    categories= Category.objects.all()
    context = {
        'expense': expense,
        'values': expense,
        'categories': categories
    }
    if request.method == 'GET':
        return render(request, '_dashboard/expense_edit.html', context )
    else:
     if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, '_dashboard/add_expenses.html', context)
    

        
        description = request.POST['description']
        date = request.POST['date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'Description is required')
            return render(request, '_dashboard/add_expenses.html', context)
        if not date:
            messages.error(request, 'Date is required')
            return render(request, '_dashboard/add_expenses.html', context)
        
        # Pushing the records in the database
        Expense.objects.create(owner=request.user,amount=amount, date=date, category=category, description=description)
        expense.owner=request.user
        expense.amount=amount 
        expense.date=date 
        expense.category=category
        expense.description=description

        expense.save()
        messages.success(request, 'Expense updated successfully')

        return redirect( 'dashboard:dashboard')
@login_required(login_url='/accounts/login')
def delete_expense(request, id):
    expense=Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'Expense removed')
    return redirect( 'dashboard:dashboard')

# endpoint for charts
@login_required(login_url='/accounts/login')
def expense_category_summary(request):
    todays_date= datetime.date.today() # Gets today's date
    six_months_ago= todays_date-datetime.timedelta(days=360) # Represents a duration of 360 days
    expenses=Expense.objects.filter(owner=request.user,date__gte=six_months_ago, date__lte=todays_date)
    # creating a dictionary to store each category as a key and its total expenses as the value
    finalrep= {}
    
    # Function to return expenses based on category
    def get_category(expense):
        return expense.category
    category_list= list(set(map(get_category, expenses)))
    # Function to return the calculted expenses of each category
    def get_expense_category_amount(category):
        amount= 0
        filter_by_category = expenses.filter(category= category)
        # To sum up the amounts of all filtered expenses
        for item in filter_by_category:
            amount += item.amount 
        return amount
    
    for i in expenses:
        for j in category_list:
            finalrep[j]=get_expense_category_amount(j)

    return JsonResponse({'expense_category_date': finalrep},safe=False)          

@login_required(login_url='/accounts/login')
def stats(request):
    return render(request, '_dashboard/stats.html')
