from django import forms
from waybill.models import Customer,Waybill


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		exclude = ['user']

	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		self.fields['real_name'].label = "真实姓名"
		self.fields['company'].label = "公司名"
		self.fields['phone_number'].label = "手机号码"
		self.fields['store'].label = "仓库"
		self.fields['client_channel'].label = "客户渠道"
		self.fields['country'].label = "国家"
		self.fields['province'].label = "省份"
		self.fields['city'].label = "城市"
		self.fields['street'].label = "详细地址（区县、街道门牌号）"

class WaybillForm(forms.ModelForm):
	class Meta:
		model = Waybill
		exclude = ['user','waybill_number','create_time']

	def __init__(self, *args, **kwargs):
		super(WaybillForm, self).__init__(*args, **kwargs)
		self.fields['order_number'].label = "订单号"
		self.fields['store'].label = "仓库"
		self.fields['client_channel'].label = "客户渠道"

		self.fields['from_person_name'].label = "发件人姓名"
		self.fields['from_company'].label = "发件人公司"
		self.fields['from_phone_num'].label = "发件人手机号码"
		self.fields['from_country'].label = "发件人国家"
		self.fields['from_province'].label = "发件人省、州"
		self.fields['from_city'].label = "发件人城市"
		self.fields['from_street'].label = "发件人街道详细"

		self.fields['to_person_name'].label = "收件人姓名"
		self.fields['to_company'].label = "收件人公司"
		self.fields['to_phone_num'].label = "收件人手机号码"
		self.fields['to_country'].label = "收件人国家"
		self.fields['to_province'].label = "收件人省、州"
		self.fields['to_city'].label = "收件人城市"
		self.fields['to_street'].label = "收件人街道详细"

		self.fields['goods_detail'].label = "物品描述"
		self.fields['goods_numbers'].label = "物品数量"
		self.fields['currency'].label = "货币单位"
		self.fields['single_price'].label = "单价"
		self.fields['total_price'].label = "总价"
		self.fields['package_numbers'].label = "包裹数量"
		self.fields['weight'].label = "总重量(KG)"
		self.fields['remark'].label = "备注"
