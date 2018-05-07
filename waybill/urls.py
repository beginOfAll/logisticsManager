from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.start, name='start'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^register/$', views.add_user, name='register'),
	url(r'^validate/$', views.validate, name='validate'),
	url(r'^userLogout/$', views.user_logout, name='userLogout'),
	url(r'^index/$', views.index, name='index'),
	url(r'^customer/$', views.customerInfo, name='customer'),
	url(r'^getCustomer/$', views.customerGet, name='getCustomer'),
	url(r'^createWaybill/$', views.createWaybill, name='createWaybill'),
	url(r'^waybillList/$', views.getWaybillListByUser, name='waybillList'),
	url(r'^waybillDetailed/', views.getWaybillDetailed, name='waybillDetailed')
]