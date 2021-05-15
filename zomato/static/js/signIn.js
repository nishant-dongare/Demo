let submitButton = document.getElementById('submitButton');
let email = document.getElementsByClassName('text')[0];
let pwd = document.getElementsByClassName('text')[1];
let emailReg = /^([a-zA-Z0-9\.-]+)@([a-zA-Z0-9-]+)\.([a-z]{2,20})$/;
let pwdReg = /^([a-zA-Z0-9\.!#$%&'*+-/=?^`.{|}~-]{8,20})$/;

submitButton.onclick = function(){
    if(emailReg.test(email.value) && pwdReg.test(pwd.value)){
        window.open(file, "_self");
        return true
    }
    else{
        alert('Invalid Email or Password.')
        return false;   
    }
}
