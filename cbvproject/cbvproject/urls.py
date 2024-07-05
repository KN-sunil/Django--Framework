
from django.contrib import admin
from django.urls import path
from cbapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("cbv",views.HelloworldView.as_view()),
    path("demo",views.getHelloworld)
]
