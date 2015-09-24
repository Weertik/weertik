$(document).ready(function() {
var msg="";
var elements = document.getElementsByTagName("INPUT");

for (var i = 0; i < elements.length; i++) {
   elements[i].oninvalid =function(e) {
        if (!e.target.validity.valid) {
        switch(e.target.id){
            case 'password' :
            e.target.setCustomValidity("Contraseña incorrecta");break;
            case 'username' :
            e.target.setCustomValidity("Usuario incorrecto");break;
            case 'id_email' :
            e.target.setCustomValidity("Email incorrecto");break;
            case 'id_email_repeat' :
            e.target.setCustomValidity("Email incorrecto");break;
        default : e.target.setCustomValidity("No puede estar vacío");break;

        }
       }
    };
   elements[i].oninput = function(e) {
        e.target.setCustomValidity(msg);
    };
}
})
