let boton = document.getElementById('reporte');
boton.addEventListener('click', function(evento) {
    evento.preventDefault();

    let contenedor = document.getElementById('contenedor');

    if (contenedor.classList.contains('d-none')) {
        // Mostrar las tablas
        contenedor.classList.remove('d-none');
    } else {
        // Ocultar las tablas
        contenedor.classList.add('d-none');
    }

    let nombreUsuario = document.getElementById('nombre').value;
    let mensaje = document.getElementById('mensaje');
    mensaje.textContent = `Apreciado usuario ${nombreUsuario}, hemos generado su reporte`;
});


//Cambia la imagen dependiendo del boton de menu de opciones que se seleccione
function cambiarImagen(imagenId, nuevaRuta) {
    var imagen = document.getElementById(imagenId);
    imagen.src = nuevaRuta;
}

//Cambia el color de los boton cuando le da clic
const btnReporte = document.getElementById('reporte');

btnReporte.addEventListener('click', function() {
    this.classList.toggle('clicked');
});

// VENTANA MODAL
// Obtener los elementos del DOM
// Obtener los elementos del DOM
var yarumal = document.getElementById("YarumalVista");
var stafeantioquia = document.getElementById("StaFeAntioquiaVista");
var caucasia = document.getElementById("CaucasiaVista");
var belmira = document.getElementById("BelmiraVista");
var bello = document.getElementById("BelloVista");
var caramanta = document.getElementById("CaramantaVista");
var yarumalbtn = document.getElementById("Yarumal");
var stafeantioquiabtn = document.getElementById("StaFeAntioquia");
var caucasiabtn = document.getElementById("Caucasia");
var belmirabtn = document.getElementById("Belmira");
var bellobtn = document.getElementById("Bello");
var caramantabtn = document.getElementById("Caramanta");
var span1 = document.getElementsByClassName("close")[0];
var span2 = document.getElementsByClassName("close")[1];
var span3 = document.getElementsByClassName("close")[2];
var span4 = document.getElementsByClassName("close")[3];
var span5 = document.getElementsByClassName("close")[4];
var span6 = document.getElementsByClassName("close")[5];


yarumalbtn.onclick = function() {
    yarumal.style.display = "block";
}

stafeantioquiabtn.onclick = function() {
    stafeantioquia.style.display = "block";
}

caucasiabtn.onclick = function() {
    caucasia.style.display = "block";
}

belmirabtn.onclick = function() {
    belmira.style.display = "block";
}

bellobtn.onclick = function() {
    bello.style.display = "block";
}

caramantabtn.onclick = function() {
    caramanta.style.display = "block";
}

// Cerrar Modales al hacer clic en la "X"
span1.onclick = function() {
    yarumal.style.display = "none";
}

span2.onclick = function() {
    stafeantioquia.style.display = "none";
}

span3.onclick = function() {
    caucasia.style.display = "none";
}

span4.onclick = function() {
    belmira.style.display = "none";
}

span5.onclick = function() {
    bello.style.display = "none";
}

span6.onclick = function() {
    caramanta.style.display = "none";
}

// Cerrar los modales al hacer clic fuera de ellos
window.onclick = function(event) {
    if (event.target == yarumal) {
        yarumal.style.display = "none";
    }

    if (event.target == stafeantioquia) {
        stafeantioquia.style.display = "none";
    }
    
    if (event.target == caucasia) {
        cauca.style.display = "none";
    }

    if (event.target == belmira) {
        belmira.style.display = "none";
    }

    if (event.target == bello) {
        bello.style.display = "none";
    }

    if (event.target == caramanta) {
        caramanta.style.display = "none";
    }
}
