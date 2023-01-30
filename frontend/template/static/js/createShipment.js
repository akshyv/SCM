async function createShipment(){
    let user_name = ""
    let Invoice_no = document.querySelector("#invoice_no").value
    let container_no = document.querySelector("#container_no").value
    let shipmentDescription = document.querySelector("#shipment_description").value                
    let description_pattern = new RegExp("[A-Za-z0-9? ,_-]+$")
    if (description_pattern.test(shipmentDescription)){
        var shipment_description = await shipmentDescription
    } else {
        shipment_description = ''
        alert ("no special character in shipment Description")
    }
    let route_details = document.querySelector("#route_details").value
    let goods_type = document.querySelector("#goods_type").value
    let device = document.querySelector("#device").value
    let expected_delivery_date = document.querySelector("#expected_delivery_date").value
    let PONumber = document.querySelector("#po_no").value
    if (PONumber.toString().length == 6){
        var PO_number = await PONumber
    }
    else {
        PO_number = null
        alert("Type Six digit for the po_number")
    }
    let delivery_no = document.querySelector("#delivery_no").value
    let NDC_no = document.querySelector("#ndc_no").value
    let batch_id = document.querySelector("#batch_id").value
    let Serial_no_of_goods = document.querySelector("#serial_no").value                

    $.ajax({
    
    url:"http://"+window.location.hostname+":8000/add_shipment",
    type:"POST",
    headers:{"Authorization": 'Bearer ' + localStorage.getItem('access_token'),
},
    contentType:"application/json",
    data:JSON.stringify({
        user_name:user_name,
        Invoice_no:Invoice_no,
        container_no:container_no,
        shipment_description:shipment_description,
        route_details:route_details,
        goods_type:goods_type,
        device:device,
        expected_delivery_date:expected_delivery_date,
        PO_number:PO_number,
        delivery_no:delivery_no,
        NDC_no:NDC_no,
        batch_id:batch_id,
        Serial_no_of_goods:Serial_no_of_goods,
    }),
    success:function(data) {

     window.location.href = "http://"+window.location.hostname+":5501/../../../template/views/home.html";
        return(data)
    },
    error: function(xhr, ajaxOptions, thrownError){
        alert("fill all details")
    }
    })
}