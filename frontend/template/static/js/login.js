function authorization() {
    let userName = document.querySelector("#username").value
    let passWord = document.querySelector("#password").value
    var data = new URLSearchParams();
    var details = {
'username': userName,
'password': passWord,
};

var formBody = [];
for (var property in details) {
var encodedKey = encodeURIComponent(property);
var encodedValue = encodeURIComponent(details[property]);
formBody.push(encodedKey + "=" + encodedValue);
}
formBody = formBody.join("&");

    $.ajax({
 
   url: "http://"+window.location.hostname+":8000/login",
  //  headers:{
  //   "Access-Control-Allow-Headers":"Content-Type",
  //   "Access-Control-Allow-Origin":"http://localhost:8000/login",
  //   "Access-Control-Allow-Methods":"OPTIONS,POST,GET,",
  //  },
    type:"POST",
    dataType: "json", 
    data: formBody,
    success:function(data) {
        localStorage.setItem("access_token", data.access_token),
        localStorage.setItem("refresh_token", data.refresh_token)
        window.location.href = "home.html"       
    },
    error: function (xhr, ajaxOptions, thrownError) {
        alert("Username or Password mismatched");
        // alert(thrownError);
    }
    });
}
  (function () {
    const fonts = ["cursive", "sans-serif", "serif", "monospace"];
    let captchaValue = "";
    function generateCaptcha() {
      let value = btoa(Math.random() * 1000000000);
      value = value.substr(0, 5 + Math.random() * 5);
      captchaValue = value;
    }
    function setCaptcha() {
      let html = captchaValue
        .split("")
        .map((char) => {
          const rotate = -20 + Math.trunc(Math.random() * 30);
          const font = Math.trunc(Math.random() * fonts.length);
          return `<span style="transform:rotate(${rotate}deg);
              font-family:${fonts[font]}"
              >${char}</span>`;
        })
        .join("");
      document.querySelector(".login-form .captcha .preview").innerHTML = html;
    }
    function initCaptcha() {
      document
        .querySelector(".login-form .captcha .captcha-refresh")
        .addEventListener("click", function () {
          generateCaptcha();
          setCaptcha();
        });
      generateCaptcha();
      setCaptcha();
    }
    initCaptcha();
  
    document
      .querySelector("#login-btn")
      .addEventListener("click", function () {
        let inputCaptchaValue = document.querySelector(
          ".login-form .captcha input"
        ).value;
        if (inputCaptchaValue === captchaValue) {
          let userName = document.querySelector("#username").value;
          let passWord = document.querySelector("#password").value;
          accessToken = authorization(userName, passWord);
        } else {
          alert("Invalid Captcha");
        }
      });
  })();

  
