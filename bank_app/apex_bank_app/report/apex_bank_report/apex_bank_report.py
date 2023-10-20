# Copyright (c) 2023, Montego-arch and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe


def execute(filters=None):
	return get_columns(), get_data(filters)


def get_data(filters):
	_from, to = filters.get('from'), filters.get('to') #date range
	#conditions
	conditions = " AND 1=1 "
	if(filters.get('apex')):conditions += f" AND apex LIKE '%{filters.get('apex')}' "
	if(filters.get('account_manager')):conditions += f" AND account_manager='{filters.get('account_manager')}' "
	if(filters.get('account_status')):conditions += f" AND account_status='{filters.get('account_status')}' "

		#SQL Query
	data = frappe.db.sql(f"""SELECT name, customer_name, address, apex_type, account_status,
					  account_balance, charges, total_balance,account_manager, manager_name
					  FROM `tabApex` WHERE (creation BETWEEN '{_from}' AND '{to}') {conditions};""")
	return data



def get_columns():
	return [
		"ID:Link/Apex:70",
		"Customer Name:Data:150",
		"Address: Data:150",
		"Account Status: Data:80"
		"Account Balance: Currency:150",
		"Charges: Percent:50",
		"Total Balance: Currency:100",
		"Account Manager: Data:150",
		"Manager Name:Data:150"
	]
