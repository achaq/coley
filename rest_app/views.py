from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import sys
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error 
from matplotlib import pyplot as plt
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings 
import plotly.plotly as py
import plotly.graph_objs as go
from keras import backend as K
import tensorflow as tf
from .models import compound
from .forms import CompoundCreateForm


from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



def home(request):
	context={
		'compounds':compound.objects.all()
	}
	print("it is in ")
	return render(request,'rest_app/home.html',context)
def about(request):
	return render(request,'rest_app/about.html',{'title':'about_title'})
def project(request):
	return render(request,'rest_app/project.html')

def newmat(request):
	return render(request,'rest_app/newmat.html')


def fitting(request):
	#labels = 'pvc_k_67','pvc_H2' ,'TIO2', 'NOIR','BLEU','Lubricant'
	#sizes = [95.5,4.5, 0.1, 0.01,0.05,25]
	#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','b']
	#explode = (0,0.1,0.2, 0.3, 0.4, 0.5)  # explode 1st slice
	
	# Plot
	#plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.4f%%', shadow=True, startangle=180)
	#plt.savefig('rest_app/static/rest_app/fitting.png')
	#plt.close()
	context = {
               'compound' : { 'pvc' : 100, 'PA310' : 1.6 ,
               'PED' : 0.45, 'GMS' : 0.41 ,
               'DIN' : 1.47, 'HSE' : 1.93 ,
				'BLEU' : 0, 'VIOLET' : 0.01 ,
				'TIO2' : 1.55,
				'NOIR' : 0, 'SCA' : 0 ,
				'FM50' : 0, 'Kane' : 0 ,
				'MBN' : 0, '3TS' : 0 ,
               },

     			'price' : { 'pvc_k' : 9.94, 'PA310' : 33.45 ,
               'PED' : 43.15, 'GMS' : 17.49 ,
               'DIN' : 74.94, 'HSE' : 15.61 ,
				'BLEU' : 53.75, 'VIOLET' : 86.81 ,
				'TIO2' : 34.3,
				'NOIR' : 86.4, 'SCA' : 16.38 ,
				'FM50' : 23.04, 'Kane' : 26.08 ,
				'MBN' : 20.00, '3TS' : 1.28 ,
               },

	}
	
	return render(request,'rest_app/fitting.html',context)
	



def pressure(request):
	context = {
               'compound' : { 'pvc_k' : 95.5, 'pvc_H2' : 4.5 ,
               'TIO2' : 0.1, 'NOIR' : 0.01 ,
               'BLEU' : 0.05, 'Lubricant' : 25.0 ,},

     			'price' : { 'pvc_k' : 9.94, 'pvc_H2' : 7.45 ,
               'TIO2' : 34.3, 'NOIR' : 86.4 ,
               'BLEU' : 53.75, 'Lubricant' : 1.28 ,},
                         
	}
	return render(request,'rest_app/pressure.html',context)


def shoe(request):
	context = {
               'compound' : { 'pvc_k' : 95.5, 'pvc_H2' : 4.5 ,
               'TIO2' : 0.1, 'NOIR' : 0.01 ,
               'BLEU' : 0.05, 'Lubricant' : 25.0 ,},

     			'price' : { 'pvc_k' : 9.94, 'pvc_H2' : 7.45 ,
               'TIO2' : 34.3, 'NOIR' : 86.4 ,
               'BLEU' : 53.75, 'Lubricant' : 1.28 ,},
                         
	}
	return render(request,'rest_app/shoe.html',context)

def sheet(request):
	context = {
               'compound' : { 'pvc_k' : 95.5, 'pvc_H2' : 4.5 ,
               'TIO2' : 0.1, 'NOIR' : 0.01 ,
               'BLEU' : 0.05, 'Lubricant' : 25.0 ,},

     			'price' : { 'pvc_k' : 9.94, 'pvc_H2' : 7.45 ,
               'TIO2' : 34.3, 'NOIR' : 86.4 ,
               'BLEU' : 53.75, 'Lubricant' : 1.28 ,},
                         
	}
	return render(request,'rest_app/sheet.html',context)

def cable(request):
	context = {
               'compound' : { 'pvc_k' : 95.5, 'pvc_H2' : 4.5 ,
               'TIO2' : 0.1, 'NOIR' : 0.01 ,
               'BLEU' : 0.05, 'Lubricant' : 25.0 ,},

     			'price' : { 'pvc_k' : 9.94, 'pvc_H2' : 7.45 ,
               'TIO2' : 34.3, 'NOIR' : 86.4 ,
               'BLEU' : 53.75, 'Lubricant' : 1.28 ,},
                         
	}
	return render(request,'rest_app/cable.html',context)




class compoundListView(LoginRequiredMixin,ListView):
    model = compound
    template_name = 'rest_app/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'compounds'
    ordering = ['-date_posted']


class compoundDetailView(DetailView):
    model = compound


class compoundCreateView(LoginRequiredMixin, CreateView):
    template_name='rest_app/compound_form.html'
    form_class = CompoundCreateForm
#fields = ['title', 'content']
    #fields=['formula_name','extensibility','stability','ductibility','toughness','strenght','pvc_k','stabilizer_type','stabilizer','chalk','impact_modifier']
    def form_valid(self, form):
        form.instance.author = self.request.user
        form = super(compoundCreateView, self).form_valid(form)
        return form

######here !
class compoundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = compound
    fields=['formula_name','extensibility','stability','ductibility','toughness','strenght','pvc_k','stabilizer_type','stabilizer','chalk','impact_modifier']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form = super(compoundUpdateView, self).form_valid(form)
        return form



    def test_func(self):
        compound = self.get_object()
        if self.request.user == compound.author:
            return True
        return False


class compoundDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = compound
    success_url = '/'

    def test_func(self):
        compound = self.get_object()
        if self.request.user == compound.author:
            return True
        return False


















def calculated(request):
	#graph = tf.get_default_graph()
	#put_params = QueryDict(request.body)
	extensibility=float(request.GET["extensibility"])
	stability=float(request.GET["stability"])
	ductibility=float(request.GET["ductibility"])
	toughness=float(request.GET["toughness"])
	strenght=float(request.GET["strenght"])
	
	#print(train.head())
	# The Input Layer :
	NN_model2 = Sequential()
	NN_model2.add(Dense(128, kernel_initializer='normal',input_dim = 5, activation='relu'))

	# The Hidden Layers :
	NN_model2.add(Dense(256, kernel_initializer='normal',activation='relu'))
	NN_model2.add(Dense(256, kernel_initializer='normal',activation='relu'))
	NN_model2.add(Dense(256, kernel_initializer='normal',activation='relu'))

	# The Output Layer :
	NN_model2.add(Dense(7, kernel_initializer='normal',activation='linear'))
	NN_model2.summary()
	# Compile the network :
	NN_model2.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])
	#NN_model2.summary()
	pressure_pipe = pd.DataFrame(np.random.randint(low=0, high=13, size=(1, 5)),columns=['Tensile_S','extensibility','Density','Stability','toughness'])
	pressure_pipe['Tensile_S']=strenght
	pressure_pipe['extensibility']=extensibility
	pressure_pipe['Density']=ductibility
	pressure_pipe['Stability']=stability
	pressure_pipe['toughness']=toughness


	wights_file = 'Weights-276--0.59837.hdf5' # choose the best checkpoint 
	NN_model2.load_weights(wights_file) # load it
	NN_model2.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])
	predictions = NN_model2.predict(pressure_pipe[['Tensile_S','extensibility','Density','Stability','toughness']])
	#print(predictions)
	if(predictions[0][3]>predictions[0][4]):
		stri="organic_stabilizer"
	elif predictions[0][5]>predictions[0][4]:
		stri="lead_stabilizer"
	else :
		stri="Ca_Z_stabilizer"
	ts=int(predictions[0][0])
	ex=int(predictions[0][1])
	st=int(predictions[0][2])
	stabil=int(predictions[0][6])
	cara=[
	{
	'pre0':ts,
	'pre1':ex,
	'pre2':st,
	'pre6':stabil,
	'stri':stri
	}]
	context={
	'cara':cara
	}
	labels = 'pvc_k_67', 'chalk', 'stabilizer','impact_modifier'
	sizes = [100, st, st,stabil]
	colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
	explode = (0.1, 0.2, 0.3, 0.4)  # explode 1st slice
	
	# Plot
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.4f%%', shadow=True, startangle=180)
	plt.savefig('rest_app/static/rest_app/composition.png')
	plt.close()
	#plt.axis('equal')
	s = pd.Series([extensibility, stability, ductibility,toughness,strenght])
	fig, ax = plt.subplots()
	s.plot.bar()
	fig.savefig('rest_app/static/rest_app/carac.png')
	plt.close()
	print("---------------------request--------------------")
	K.clear_session()
	return render(request,'rest_app/calculated.html',context)
	