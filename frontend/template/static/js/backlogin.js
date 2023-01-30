const forms = document.querySelector('.forms'),
      pwShowHide = document.querySelectorAll('.eye-icon'),
      links = document.querySelectorAll('.link');

console.log(forms,pwShowHide,links)

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", ()=>{
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");
        console.log(pwFields)
    })
})

links.forEach(link => {
    link.addEventListener("click", e =>{
        e.preventDefault();
        forms.classList.toggle("show-signup")
    })
})