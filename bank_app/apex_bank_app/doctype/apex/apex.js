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
		// Compute total
		frm.compute_total = function(frm){
			let total = 0;
			// loop through the child table
			frm.doc.financial_services.forEach(d=>{
				total = total - d.service_price;
			})
			// new_total
			let new_total = frm.doc.account_balance + total;
			if(frm.doc.charges){
				new_total = new_total - (new_total * (frm.doc.charges/100))
			}
			console.log(new_total);
			// set total balance
			frm.set_value('total_balance', new_total);
		}
	},
	refresh: function(frm) {
		frm.add_custom_button('Say Hi', () => {
			frappe.prompt('Address', ({ value }) => {
				if(value){
					frm.set_value('address', value);
					frm.refresh_field('address')
					frappe.msgprint(__(`Address field updated with${value}`));

				}
			})	
		}, "Actions");
		// check account type
		frm.add_custom_button('Check Account Type', ()=>{
			let apex_type = frm.doc.apex_type
			console.log(apex_type);
			// MAKE AJAX CALL
			frappe.call({
				method: "bank_app.apex_bank_app.doctype.apex.api.check_account_types", //dotted path to server method
				args: {'apex_type': apex_type},
				callback: function(r) {
					// code snippet
					console.log(r);
					if(r.message.length>0){
						let header = `<h3>Below account is ${apex_type}</h3>`;
						let body = ``;
						r.message.forEach(d=>{
							let cont = `<p>Name: ${d.name}: <a href='/app/apex/${d.name}'>Visit</a></p>`;
							body = body + cont;
						})
						let all = header + body;
							// message print
						frappe.msgprint(__(all));
					}
				
				}
			});
			
		}, "Actions");
	},
	account_balance: function(frm){
		frm.compute_total(frm);
	},
	charges: function(frm){
		frm.compute_total(frm);
	}
});


// FINANCIAL SERVICES CHILD TABLE

frappe.ui.form.on('Apex Service Details', {
	services: function(frm, cdt, cdn){
		// grab the entire service
		let row = locals[cdt][cdn];
		frm.check_student_account_against_business_consulting(frm, row)
		frm.check_services_duplicates(frm, row, row.services);
		frm.compute_total(frm);
		
		// console.log(row);
	},
	financial_services_remove: function(frm, cdt, cdn){
		frm.compute_total(frm);
	}	
});