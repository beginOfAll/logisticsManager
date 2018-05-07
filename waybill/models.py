from django.db import models
from django.contrib.auth.models import User
import json

CURRENCY_CHOICES = (
	('CNY', '人民币'),
	('USD', '美元'),
	('GBP', '英镑'),
	('JPY', '日元'),
	('AUD', '澳元'),
	('EUR', '欧元')
)


class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# 真实姓名
	real_name = models.CharField(max_length=30)
	# 公司
	company = models.CharField(max_length=100)
	# 手机号码
	phone_number = models.CharField(max_length=20)
	# 仓库
	store = models.CharField(max_length=50)
	# 客户渠道
	client_channel = models.CharField(max_length=50)
	# 国家
	country = models.CharField(max_length=50)
	# 省、州
	province = models.CharField(max_length=50)
	# 城市
	city = models.CharField(max_length=50)
	# 街道
	street = models.CharField(max_length=100)

	def toDict(self):
		d = dict()
		d['user_name'] = self.user.username
		d['real_name'] = self.real_name
		d['company'] = self.company
		d['phone_number'] = self.phone_number
		d['country'] = self.country
		d['province'] = self.province
		d['city'] = self.city
		d['street'] = self.street
		d['store'] = self.store
		d['client_channel'] = self.client_channel
		return d

	def toJson(self):
		return json.dumps(self.toDict())


class Waybill(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# 运单号
	waybill_number = models.CharField(max_length=50)
	# 创建时间
	create_time = models.DateTimeField()
	# 订单号
	order_number = models.CharField(max_length=50)
	# 仓库
	store = models.CharField(max_length=50)
	# 客户渠道
	client_channel = models.CharField(max_length=50)

	#### 发件人信息
	#  发件人姓名
	from_person_name = models.CharField(max_length=100, default="")
	# 发件人公司
	from_company = models.CharField(max_length=100, default="")
	# 发件人手机号码
	from_phone_num = models.CharField(max_length=100, default="")
	# 发件人国家
	from_country = models.CharField(max_length=50, default="")
	# 省、州
	from_province = models.CharField(max_length=50, default="")
	# 城市
	from_city = models.CharField(max_length=50, default="")
	# 街道
	from_street = models.CharField(max_length=100, default="")

	#### 收件人信息
	# 收件人姓名
	to_person_name = models.CharField(max_length=100)
	# 收件人公司
	to_company = models.CharField(max_length=100)
	# 收件人手机号码
	to_phone_num = models.CharField(max_length=100)
	# 收件人国家
	to_country = models.CharField(max_length=50)
	# 省、州
	to_province = models.CharField(max_length=50)
	# 城市
	to_city = models.CharField(max_length=50)
	# 街道
	to_street = models.CharField(max_length=100)

	#### 物品详情
	# 物品描述
	goods_detail = models.CharField(max_length=100)
	# 物品数量
	goods_numbers = models.IntegerField()
	# 货币单位
	currency = models.CharField(max_length=10,choices=CURRENCY_CHOICES)
	# 单价
	single_price = models.FloatField()
	# 总价
	total_price = models.FloatField()
	# 包裹数量
	package_numbers = models.IntegerField()
	# 总重量
	weight = models.FloatField()

	# 备注
	remark = models.CharField(max_length=200)
