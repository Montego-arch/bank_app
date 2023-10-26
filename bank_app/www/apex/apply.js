$('#apex-transactions').submit(e=>{
    e.preventDefault();
    // upload method
    makecall();
    
})

// upload transactions
let makecall = async()=>{
    let formdata = $('#apex-transactions').serializeArray().reduce(
        (obj, item)=>(obj[item.name]=item.value, obj), {}
    );
    //post to API
    if(formdata){
        let res = await $.ajax({
            url: '/api/resource/Apex Transactions',
            type: 'POST',
            headers: {
                'Content-Type': 'transfer/JSON',
                'X-Frappe-CSRF-Token': frappe.csrf_token
            },
            data: JSON.stringify(formdata),
            success: function(data){
                return data
            },
            error: function(data){
                return data
            }
           
        })
        console.log(res);
    }
}