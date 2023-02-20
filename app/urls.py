from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('home/',views.home,name='home'),
    path('crud/', views.crud,name='crud'),
    path('edit/<int:id>/', views.Edit,name='edit'),
    path('del/<int:id>/', views.Delete,name='delete'),
    path('add/', views.add_data,name='add'),

    path('emp_api/',views.EmployeAPI().as_view()),


    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('shop/',views.shop,name='shop'),
    path('design/',views.design,name='design'),
    path('contact/',views.contact,name='contact'),
    
]
