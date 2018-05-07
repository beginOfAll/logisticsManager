from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
import datetime, functools
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from waybill.forms import CustomerForm, WaybillForm
from waybill.models import Customer, Waybill
from django.utils import timezone

JsonResponse = functools.partial(JsonResponse, safe=False, json_dumps_params={'ensure_ascii': False})


# Create your views here.
def start(request):
	return redirect(login_view)


def login_view(request):
	return render(request, 'waybill/login.html')


def add_user(request):
	res = False
	name = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	try:
		User.objects.create_user(name, email, password=password)
		res = True
	except:
		print('create_user failed')
	return JsonResponse(res)


def validate(request):
	res = False
	name = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=name, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			print("User is valid, active and authenticated")
			# return redirect(index)
			res = True
		else:
			print("The password is valid, but the account has been disabled!")
	else:
		print("The username and password were incorrect.")
	return JsonResponse(res)


def user_logout(request):
	logout(request)
	return redirect(login_view)


@login_required
def index(request):
	g = Group.objects.get(name="manager")
	u = g.user_set.all()
	context = {'username': request.user.username}
	return render(request, 'waybill/index.html', context)


@login_required
def customerInfo(request):
	user = User.objects.get(username=request.user.username)
	if request.method == "POST":
		try:
			cuModel = Customer.objects.get(user=user)
		except:
			cuModel = Customer(user=user)
		cuForm = CustomerForm(request.POST, instance=cuModel)
		if cuForm.is_valid():
			cuForm.save()
			message = "保存成功！"
		else:
			message = "表单填写错误！"
	else:
		try:
			cuModel = Customer.objects.get(user=user)
			cuForm = CustomerForm(instance=cuModel)
		except:
			cuForm = CustomerForm()
		message = None
	return render(request, "waybill/customer.html", {"form": cuForm, 'username': user.username, 'message': message})


@login_required
def customerGet(request):
	user = User.objects.get(username=request.user.username)
	cuModel = None
	if request.method == "GET" and request.is_ajax():
		try:
			cuModel = Customer.objects.get(user=user).toDict()
		except:
			pass
	return JsonResponse(cuModel)


@login_required
def createWaybill(request):
	user = User.objects.get(username=request.user.username)
	message = None
	if request.method == "POST":
		wb_number = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[2:-3]
		wbModel = Waybill(user=user, waybill_number=wb_number, create_time=timezone.now())
		wbForm = WaybillForm(request.POST, instance=wbModel)
		if wbForm.is_valid():
			wbForm.save()
			message = "提交成功！"
		else:
			message = "表单填写错误！"
	else:
		try:
			cuModel = Customer.objects.get(user=user)
			wbForm = WaybillForm(initial={'store': cuModel.store, 'client_channel': cuModel.client_channel,
										  'from_person_name': cuModel.real_name, 'from_company': cuModel.company,
										  'from_phone_num': cuModel.phone_number, 'from_country': cuModel.country,
										  'from_province': cuModel.province, 'from_city': cuModel.city,
										  'from_street': cuModel.street})
		except:
			wbForm = WaybillForm()
	return render(request, "waybill/waybill_form.html", {"form": wbForm, 'username': user.username, 'message': message})


@login_required
def getWaybillListByUser(request):
	res = list()
	user = User.objects.get(username=request.user.username)
	if request.method == "GET" and request.is_ajax():
		waybills = Waybill.objects.filter(user=user).values('waybill_number', 'create_time', 'to_person_name')
		for item in waybills:
			res.append(item)
	return JsonResponse(res)


@login_required
def getWaybillDetailed(request):
	user = User.objects.get(username=request.user.username)
	if request.method == "GET":
		wbnum = request.GET['wbNumber']
		waybill = get_object_or_404(Waybill, user=user, waybill_number=wbnum)
		return render(request, "waybill/waybillDetailed.html", {"waybill": waybill, 'username': user.username})
