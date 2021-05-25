from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pizza,Burger
from django.views.decorators.csrf import csrf_exempt
from .forms import NewUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
	ctx={'active_link':'home'}
	return render(request,"food/home.html",ctx)

def burger(request):
	burgers=Burger.objects.all()
	ctx={'burgers':burgers,'active_link':'burger'}
	return render(request,"food/burger.html",ctx)

def pizza(request):
	pizzas=Pizza.objects.all()
	ctx={'pizzas':pizzas,'active_link':'pizza'}
	return render(request,"food/pizza.html",ctx)

@csrf_exempt
def order(request):
	if request.is_ajax():
		note=request.POST.get('note')
		print(note)
		order=request.POST.get('orders')
		print(order)
	ctx={'active_link':'order'}
	return render(request,"food/order.html",ctx)

'''
def success(request):
	order=request.session['order']
	ctx={'order':order}
	return render(request,'food/success.html',ctx)
'''

def signup(request):
	ctx={}
	if request.POST:
		form=NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			ctx['form']=form
	else:
		form=NewUserForm()
		ctx['form']=form
	return render(request,'food/signup.html',ctx)

def logIn(request):
	if request.POST:
		username=request.POST.get('username')
		pwd=request.POST.get('password')
		user=authenticate(request,username=username,password=pwd)
		if user is not None:
			login(request,user)
			redirect('home')
		else:
			messages.info(request,'username or password are incorrect')
	ctx={'active_link':'login'}
	return render(request,'food/login.html',ctx)

def logOut(request):
	logout(request)
	return redirect('home')