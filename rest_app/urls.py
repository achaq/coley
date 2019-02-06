from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('newmat/', views.newmat, name='newmat'),
    path('pressure/', views.pressure, name='pressure'),
    path('fitting/', views.fitting, name='fitting'),
    path('calculated/', views.calculated, name='calculated'),
]


