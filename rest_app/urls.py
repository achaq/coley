from django.urls import path
from .views import compoundListView
from . import views

from .views import (
    compoundListView,
    compoundDetailView,
    compoundCreateView,
    compoundUpdateView,
    compoundDeleteView
)


urlpatterns = [
    path('',compoundListView.as_view() , name='home'),
    path('compound/<int:pk>/', compoundDetailView.as_view(),name='compound-detail'),
    path('compound/new/', compoundCreateView.as_view(), name='compound-create'),
    path('compound/<int:pk>/update/', compoundUpdateView.as_view(), name='compound-update'),
    path('compound/<int:pk>/delete/', compoundDeleteView.as_view(), name='compound-delete'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('newmat/', views.newmat, name='newmat'),
    path('pressure/', views.pressure, name='pressure'),
    path('fitting/', views.fitting, name='fitting'),
    path('calculated/', views.calculated, name='calculated'),
]


