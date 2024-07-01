
from django.contrib import admin
from django.urls import path
from empapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gethomepage),
    path('registration/',views.getempregpage),
    path('saveemp/', views.saveempview,name='saveemp'),
    path('saveuser/', views.saveuserview, name='saveuser'),
    path('newuser/',views.getnewuserpage),
]
