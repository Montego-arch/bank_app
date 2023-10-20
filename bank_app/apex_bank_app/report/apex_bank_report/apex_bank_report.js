// Copyright (c) 2023, Montego-arch and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Apex Bank Report"] = {
	"filters": [
		{
			"fieldname": "apex",
			"label":__("Apex Name"),
			"fieldtype": "Data",
			"width": 100,
			"reqd": 0,
		},
		{
			"fieldname": "from",
			"label":__("From Date"),
			"fieldtype": "Date",
			"width": 80,
			"reqd": 1,
			"default": dateutil.year_start()
		},
		{
			"fieldname": "to",
			"label":__("To Date"),
			"fieldtype": "Date",
			"width": 80,
			"reqd": 1,
			"default": dateutil.year_end()
		},
		{
			"fieldname": "account_manager",
			"label":__("Manager's Name"),
			"fieldtype": "Link",
			"options": "Account Manager",
			"width": 100,
			"reqd": 0,
		
		},
		{
			"fieldname": "account_status",
			"label":__("Account Status"),
			"fieldtype": "Select",
			"default": "",
			"options": ['','Savings', 'Current', 'Domiciliary'],
			"width": 100,
			"reqd": 0,
		
		},

	]
};
