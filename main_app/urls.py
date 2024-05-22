from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('mens-category/', views.mens, name='men-category'),
    path('occasional/', views.occasion, name='occasional'),
    path('formals/', views.formals, name='formals'),
    path('casuals/', views.casuals, name='casuals'),
    path('kid/', views.kid, name='kid'),
    path('product/<str:model_type>/<int:id>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
]
