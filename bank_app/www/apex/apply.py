import frappe
from frappe.model.document import Document

class Apex(Document):
	
	def after_insert(self):
		frappe.msgprint((f'Document {self.name} inserted successfully'));


	#validate service charges
	def validate(self):
		service_price = 0
		for i in self.financial_services:
			service_price+=i.service_price
		charges = 0
		
		self.total_balance = self.account_balance-service_price - ((0/100))* (self.account_balance-service_price)