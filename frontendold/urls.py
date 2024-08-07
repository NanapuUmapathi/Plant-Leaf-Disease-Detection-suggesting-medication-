from django.urls import path
from . import views
from frontend.views import home
"""
from frontend.views import create_zonerecord
from frontend.views import CalculateLabelZones
from frontend.views import geeks_view
from frontend.views import hello
from frontend.views import home
from frontend.views import create_view
from frontend.views import list_view
from frontend.views import detail_view
from frontend.views import update_view
from frontend.views import delete_view
from frontend.views import fileupload
from frontend.views import zonewisecount
from frontend.views import getfileproposed
from frontend.views import CalculateLabelZonesByLatLng
"""

urlpatterns = [
    path('home/', views.home, name='home'),

]   
#path('detail_view/', list_view),
"""
    path('listzonerecords/', views.listzonerecords, name='listzonerecords'),
    path('products/', views.products, name='products'),
    
    path('customers/', views.customers, name='customers'),
    
    path('listcustomers/', views.listcustomers, name='listcustomers'),
    path('geeks/', geeks_view),
    path('hello/', hello),
    path('create_view/', create_view),
    path('list_view/', list_view),
    path('details_view/<id>', detail_view ),
    path('update_view/<id>', update_view ),
    path('<id>/delete', delete_view ),
    path('', views.home,name="home"),
    path('languages/', views.languages, name='languages'),
    path('fileupload/', views.fileupload, name='fileupload'),
    path('csv',views.getfile)  ,
    path('csvproposed/',views.getfileproposed)  ,
    path('calculatelabelzones/',CalculateLabelZones),
    path('CalculateLabelZonesByLatLng/',CalculateLabelZonesByLatLng),
path('zonewisecount/',zonewisecount),
"""