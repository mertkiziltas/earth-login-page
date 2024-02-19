

function Auth(){
    const action = document.getElementById("action");
    let authUsername = document.getElementById("auth_username").value;
    let authPassword = document.getElementById("auth_password").value;

    let submitBtn = document.getElementById("login_button"); 

    if (authUsername == "admin"){
        alert('Login Successful');
    }
    else{
        alert("login discussed")
    }

}

let submit = document.getElementById("login_button");
submit.addEventListener('click',Auth())