# Copyright (c) 2023, Montego-arch and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Apex(Document):
	
	def after_insert(self):
		frappe.msgprint((f'Document {self.name} inserted successfully'));
	#validate
	# def validate(self):
	# 	if(self.apex_type=="Student Account"):
	# 		pass
			# for services in self.financial_services:
			# 	if(services.services=="Business Consulting"):
			# 		frappe.throw((f'<b>Student Account</b> should not have <b>{services.services}</b> service.'))

			#SQL
			# services = frappe.db.sql(f"""SELECT services FROM `tabApex Service Details` WHERE parent="000002" AND parentType="Apex" AND services="Business Consulting";""", as_dict=True)
			# print(f"""\n\n{services}""")
			# if(services):
			# 	frappe.throw((f'<b>Student Account</b> should not have <b>{services[0].services}</b> service.'))
