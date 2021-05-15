let textFields = document.getElementsByClassName('textFields');
let placeholderText = document.getElementsByClassName('placeholderText');
let placeholder = document.getElementsByClassName('placeholder');
let formText = document.getElementsByClassName('formText');
let name = formText[1].value;
let formEmail = formText[2].value;
let mobile = formText[3].value;
let cmnt = formText[4].value
let invalidInput = document.getElementsByClassName('invalidInput');
let submitButton = document.getElementsByClassName('submitButton');

let nameReg = /^([a-zA-Z]+)$/;
let emailReg = /^([a-zA-Z0-9\.-]+)@([a-zA-Z0-9-]+)\.([a-z]{2,20})$/;
let mobileReg = /^([0-9]{10})$/;
let cmntReg = /^([a-zA-Z0-9\.!#$%&'*+-/=?^`.{|}~-]+)$/;
let arr = [nameReg, emailReg, mobileReg, cmntReg];

submitButton[0].disabled = true;

function textChanges(pos, temp){
    if(temp === true){
        placeHolderChanges(textFields[pos], '1px solid rgb(17, 145, 153)', placeholder[pos], 'rgb(17, 145, 153)', 'auto', '1s ease', 'relative', '20px', '12px', '-20px');
    }
    if(temp === false){
        if(formText[pos].value == ""){
            placeHolderChanges(textFields[pos], '1px solid rgb(207, 207, 207)', placeholder[pos], ' rgb(156, 156, 156)', 'auto', '1s ease', 'relative', 'auto', '18px', '0px');
        }
        else{
            if(arr[pos-1].test(formText[pos].value)){
                invalidInput[pos-1].style.opacity = '0';
                textFields[pos].style.border = 'px solid rgb(207, 207, 207)';
            }
            else{
                invalidInput[pos-1].style.opacity = '1';
                textFields[pos].style.border = '1px solid red';
            }
        }
    }
}


function placeHolderChanges(elm1, border, elm2, color, width, tran, pos, height, fSize, mTop){
    elm1.style.border = border;
    elm2.style.color = color;
    elm2.style.width = width;
    elm2.style.transition = tran;
    elm2.style.position = pos;
    elm2.style.height = height;
    elm2.style.fontSize = fSize;
    elm2.style.marginTop = mTop;
}
