from . import __version__ as app_version

app_name = "bank_app"
app_title = "Apex Bank App"
app_publisher = "Montego-arch"
app_description = "It is a bank app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "okekeemmanuelomolola@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bank_app/css/bank_app.css"
# app_include_js = "/assets/bank_app/js/bank_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/bank_app/css/bank_app.css"
# web_include_js = "/assets/bank_app/js/bank_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bank_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bank_app.install.before_install"
# after_install = "bank_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bank_app.uninstall.before_uninstall"
# after_uninstall = "bank_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bank_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
	"Apex": {
        "validate": "bank_app.apex_bank_app.doctype.apex.events.validate",
        "on_update": "bank_app.apex_bank_app.doctype.apex.events.on_update",
        "after_insert": "bank_app.apex_bank_app.doctype.apex.events.after_insert",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"bank_app.tasks.all"
#	],
#	"daily": [
#		"bank_app.tasks.daily"
#	],
#	"hourly": [
#		"bank_app.tasks.hourly"
#	],
#	"weekly": [
#		"bank_app.tasks.weekly"
#	]
#	"monthly": [
#		"bank_app.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "bank_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "bank_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "bank_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["bank_app.utils.before_request"]
# after_request = ["bank_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["bank_app.utils.before_job"]
# after_job = ["bank_app.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"bank_app.auth.validate"
# ]

