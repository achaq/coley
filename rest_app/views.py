from django.shortcuts import render
from django.http import HttpResponse

posts=[
{
	'author':'camus',
	'title':'la peste',
	'content':'critisicism',
	'date':'augaust,27 2019'
},
{
	'author':'camus22',
	'title':'la peste22',
	'content':'critisicism22',
	'date':'augaust,22 2022'
}
]





def home(request):
	context={
		'posts':posts
	}
	return render(request,'rest_app/home.html',context)
def about(request):
	return render(request,'rest_app/about.html',{'title':'about_title'})
def project(request):
	return render(request,'rest_app/project.html')

def newmat(request):
	return render(request,'rest_app/newmat.html')


def fitting(request):
	return render(request,'rest_app/fitting.html')
	

def pressure(request):
	return render(request,'rest_app/pressure.html')

def calculated(request):
	return render(request,'rest_app/calculated.html')
	