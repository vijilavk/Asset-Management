

frappe.query_reports["Asset Report"] = {
	filters: [
		{
            "fieldname": "category",
            "label": __("Asset Category"),
            "fieldtype": "Select",
            "options": "\nLap Top\nMonitor\nFurniture\nOther",
			"default":"",
            "reqd": 0
        },
		{
			"fieldname":"status",
			"label":__("Status"),
			"fieldtype":"Select",
			"options":"\nAvailable\nAssigned\nUnder Maintenance\nRetired",
			"default":"",
		}

	]
};
