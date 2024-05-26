from django.shortcuts import render, redirect
import joblib
from .forms import SignupForm, UserLogin
from .models import User
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
import pandas as pd
data = pd.read_csv('agriculture.csv')
model = joblib.load('agricultural production optimization engine.pkl')
def home(request):
	return render(request,'predict/home.html',{'name':'shubhangi'})


def predict(request):
	value = {}
	if request.method == "POST":
		nitrogen = int(request.POST['nitrogen'])
		phosphorus = int(request.POST['phosphorus'])
		potassium = int(request.POST['potassium'])
		temperature = int(request.POST['temperature'])
		humidity = int(request.POST['humidity'])
		ph = int(request.POST['ph'])
		rainfall = int(request.POST['rainfall'])
		output = model.predict([[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]])[0]
		value['output']=output
	return render(request,'predict/predict.html',value)

def statistics(request):
	
	df = data['label'].value_counts().index
	
	return render(request,'predict/statistics.html',{'df':df})

def selectlabel(request):
	value = {}
	if request.method == "POST":
		label = request.POST.get('label')
		x = data[data['label']==label]
		n_min = x['N'].min()
		p_min = x['P'].min()
		k_min = x['K'].min()
		t_min = x['temperature'].min()
		h_min = x['humidity'].min()
		ph_min = x['ph'].min()
		rain_min = x['rainfall'].min()

		minimum = [n_min,p_min,k_min,t_min,h_min,ph_min,rain_min]

		n_mean = x['N'].mean()
		p_mean = x['P'].mean()
		k_mean = x['K'].mean()
		t_mean = x['temperature'].mean()
		h_mean = x['humidity'].mean()
		ph_mean = x['ph'].mean()
		rain_mean = x['rainfall'].mean()

		average = [n_mean,p_mean,k_mean,t_mean,h_mean,ph_mean,rain_mean]

		n_max = x['N'].max()
		p_max = x['P'].max()
		k_max = x['K'].max()
		t_max = x['temperature'].max()
		h_max = x['humidity'].max()
		ph_max = x['ph'].max()
		rain_max = x['rainfall'].max()

		maximum = [n_max,p_max,k_max,t_max,h_max,ph_max,rain_max]
		value['minimum']=minimum
		value['average']=average
		value['maximum']=maximum
		
	return render(request,'predict/statistics_show.html',value)

def average(request):
	
	df = data.iloc[0:1,:-1]
	label = data['label'].value_counts().index
	return render(request,'predict/average.html',{'df':df,'label':label})

def selectaverage(request):
	result = []
	if request.method == "POST":
		avg = request.POST.get('avg')
		labels = data['label'].value_counts().index
		for label in labels:
			result.append(data[data['label']==label][avg].mean())
	return render(request,'predict/average_show.html',{'result':result})


def climat(request):
	df = data.iloc[0:1,:-1]
	label = data['label'].value_counts().index
	return render(request,'predict/climat.html',{'df':df,'label':label})

def above(request):
	if request.method == "POST":
		condition = request.POST.get('condition')
		above = [data[data[condition]>data[condition].mean()]['label'].unique()]
		below = [data[data[condition]<data[condition].mean()]['label'].unique()]

	return render(request,'predict/above.html',{'above':above,'below':below})	

def season(request):
	summer = data[(data['temperature']>30) & (data['humidity']>50)]['label'].unique()
	winter = data[(data['temperature']<29) & (data['humidity']>30)]['label'].unique()
	rainy = data[(data['rainfall']>200) & (data['humidity']>30)]['label'].unique()
	return render(request,'predict/season.html',{'summer':summer,'winter':winter,'rainy':rainy})


def signup(request):
	error = None
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			fullname = form.cleaned_data['fullname']
			email = form.cleaned_data['email']
			mobile = form.cleaned_data['mobile']
			pas = form.cleaned_data['password']
			password = make_password(pas)

			user = User(fullname = fullname, email=email, mobile=mobile, password=password)
			email_check = user.Email_exits()
			mobile_check = user.Mobile_exits()

			if email_check:
				error = 'Email is already registered...!'
			elif mobile_check:
				error = 'Mobile is already registered...!'
			else:
				user.save()
				return redirect('login')
	else:
		form = SignupForm();
	return render(request, 'predict/signup.html', {'form':form, 'error':error})

def login(request):
	error = None
	if request.method == "POST":
		form = UserLogin(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = User()
			check_user = user.Is_user_exits(email)
			if check_user:
				if check_password(password,check_user.password):
					request.session['user_id'] = check_user.id
					return redirect('predict')
				else:
					error = 'Invalid Password...!'
			else:
				error = 'Invalid Email...!'
	else:
		form = UserLogin()
		
	return render(request, 'predict/login.html',{'form':form,'error':error})

def logout(request):
	request.session.clear()
	return redirect('home')