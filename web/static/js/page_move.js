var country;  
var gender;
function input(){     
    var input = document.getElementById("city").value; 
    var input_gender = document.getElementById("gender").value;
    gender = input_gender
    localStorage.setItem("gender",JSON.stringify(gender));    
    if (input != null ){         
        country = input.toLowerCase();  
        localStorage.setItem("city",JSON.stringify(country));  
        location.href= "http://mysite.com:8000/weather";   
    } 
    }

/*
var country;

function input(){
    var input = document.getElementById("city").value;
    var input_gender = document.getElementById("gender").value;
    if (input != null ){
        country = input.toLowerCase();
        localStorage.setItem("city",JSON.stringify(country));
        localStorage.setItem('gender',JSON.stringify(input_gender));
        // weather파일로 데이터 넘김 
    }
    else {
        location.href= "http://mysite.com:8000/index";
    }
    
    
    
    if (input_gender != null ){
        localStorage.setItem('gender',JSON.stringify(input_gender));
        // weather파일로 데이터 넘김 
    }
    else {
        location.href= "http://mysite.com:8000/index";
    }
} */
