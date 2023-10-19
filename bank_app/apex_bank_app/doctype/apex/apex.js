// Copyright (c) 2023, Montego-arch and contributors
// For license information, please see license.txt

frappe.ui.form.on('Apex', {
	setup: function(frm){
			// CHECK SERVICE DUPLICATE
			frm.check_services_duplicates = function(frm, row){
				frm.doc.financial_services.forEach(item=>{
					if(row.services=='' || row.idx==item.idx){
						// pass
					} else {
						if(row.services==item.services){
							// clear field
							row.amenity = '';
							frappe.throw(__(`${item.services} already exists in row ${item.idx}`));
							frm.refresh_field('financial_services');

					}
					}
				})
			}
			// student agaist business cons
			frm.check_student_account_against_business_consulting = function(frm, row, services){
			  if(row.services == "Business Consulting" && frm.doc.apex_type=="Student Account"){
				let services = row.services
				row.services = '';
				frappe.throw(__(`${services} cannot be rendered to a Student`));
				frm.refresh_field('financial_services');
			}
			
		}
	},
	refresh: function(frm) {
		// frm.add_custom_button('Say Hi', () => {
		// 	frappe.prompt('Address', ({ value }) => {
		// 		if(value){
		// 			frm.set_value('address', value);
		// 			frm.refresh_field('address')
		// 			frappe.msgprint(__(`Address field updated with${value}`));

		// 		}
		// 	})
			
		// });

	},
});


// FINANCIAL SERVICES CHILD TABLE

frappe.ui.form.on('Apex Service Details', {
	services: function(frm, cdt, cdn){
		// grab the entire service
		let row = locals[cdt][cdn];
		frm.check_student_account_against_business_consulting(frm, row)
		frm.check_services_duplicates(frm, row, row.services)
		// console.log(row);
	}
		
});