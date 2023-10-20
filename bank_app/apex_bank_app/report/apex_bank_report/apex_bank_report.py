# Copyright (c) 2023, Montego-arch and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe


def execute(filters=None):
	return get_columns(), get_data(filters)


def get_data(filters):
	print(f"\n\n\n\{filters}\n\n\n\n")
	return[
		['01278', 'Test Customer', 'Savings'],
		['01248', 'Test Customer 2', 'Savings']
	]

def get_columns():
	return [
		"ID:Link/Apex:70",
		"Customer Name: Data",
		"Type:Data:50"
	]
