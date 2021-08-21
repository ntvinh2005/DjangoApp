from django.urls import path

from . import views

urlpatterns=[
path('<int:id>',views.index,name="index"),
path("",views.home,name="home"),
path("subject/",views.subject,name="subject"),
path("view/",views.view,name="view"),
path("view/<str:fil>/",views.filter,name="filter")
]