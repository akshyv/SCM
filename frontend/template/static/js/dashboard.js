async function get_user(){
}
async function checkValidity(){
  var status = false;
  await $.ajax({
   
          url:"http://"+window.location.hostname+":8000/checkValidity",
          type:"GET",
          headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token'),
    },
          success:function(data) {
            status = data
          },
          error: function(xhr, ajaxOptions, thrownError){                    
              status = false
              return status
          }
  })
  return status
}
  async function shipment_redirect() {          
          console.log("redirect trigered")
          var token = await checkValidity().then((result)=>{
    
            window.location.href = "shipment.html"
          }).catch((error)=>{
      
            window.location.href = "/template/index.html"       
          })
      }
  async function data_redirect() {
    var token = await checkValidity().then((result)=>{
  
      window.location.href = "deviceData.html"
          }).catch((error)=>{
       
            window.location.href = "/template/index.html"      

          })
  }
  function logout() {
    localStorage.removeItem("access_token")
    localStorage.removeItem("refresh_token")

    window.location.href = "/template/index.html"
  }