from django.conf.urls import include, url
from add import views

urlpatterns = [
	url(r'^home/', views.home,name='home'),
    url(r'^addition/', views.addition,name='addition'),

]
