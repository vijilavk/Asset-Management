# Copyright (c) 2025, vijila and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Asset(Document):
	def validate(self):
		self.clear_value()

	def clear_value(self):
		if self.status=="Retired":
			self.assigned_to=""