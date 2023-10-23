frappe.pages['apex-transfer'].on_page_load = function(wrapper) {
	new MyPage(wrapper);
}

// PAGE CONTENT
MyPage = Class.extend({
	init: function(wrapper){
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Transfer Page',
			single_column: true
		});
		//MAKE PAGE
		this.make();
	},
	// MAKE PAGE
	make: function(){
		// grab the class
		let me = $(this);

		// body content
		// let body = `<h1></h1>`;

		//push DOM element to page
		$(frappe.render_template(frappe.bank_app_page.body, this)).appendTo(this.page.main)
	}

	//end of CLASS

})

//HTML CONTENT

let body = `
		
`;
// frappe.bank_app_page = {}
frappe.bank_app_page = {
	body: body
}

