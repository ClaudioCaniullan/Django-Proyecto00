 
// funcion login desde index html para ir a usuario2 html lineas 104 y 137// 
function EnviarDatos() {
    /**NOMBRE USUARIO */
    var VALOR_1 = "ABC";
    /**CONTRASEÑA */
    var VALOR_2 = "123";

    // validacion
            /**document.getElementById("nombrePersona").value */
        if ( document.getElementById("Nombre").value == VALOR_1 && document.getElementById("Passwordz").value == VALOR_2) {
            window.location = "usuario2.html";
        }
        else{
            window.locaton = "index.hml"
            alert("volver a intentar")
            location.reload();
        }
}