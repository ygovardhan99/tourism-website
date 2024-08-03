function validateform(){ 
    var tel=document.getElementById("phonenum").value;  

    if(tel.length<10){  
        alert("Phone number must be of atleast 10 digits!");  
        return false;  
    } else if(isNaN(tel)){
        alert("Phone number should not include character!");
        return false;
    }
    return true;
}  
