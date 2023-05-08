
//COLORES DEL ESTADO
$('td:contains("disponible")').css('color', 'blue')
$('td:contains("alquilado")').css('color', 'red')
$('td:contains("en alquiler")').css('color', 'green')
$('td:contains("en venta")').css('color', 'green')
$('td:contains("Por vender")').css('color', 'orange')
$('td:contains("vendido")').css('color', 'red')


if ($('td:contains("disponible")')) {
    $('td:contains("disponible")').html('<div class="punto-azul"></div>disponible')
}

if ($('td:contains("alquilado")')) {
    $('td:contains("alquilado")').html('<div class="punto-rojo"></div>alquilado')
}

if ($('td:contains("en alquiler")')) {
    $('td:contains("en alquiler")').html('<div class="punto-verde"></div>en alquiler')
}

if ($('td:contains("en ventar")')) {
    $('td:contains("en venta")').html('<div class="punto-verde"></div>en venta')
}

if ($('td:contains("Por vender")')) {
    $('td:contains("Por vender")').html('<div class="punto-naranja"></div>Por vender')
}

if ($('td:contains("vendido")')) {
    $('td:contains("vendido")').html('<div class="punto-rojo"></div>vendido')
}


// FUNCIONAMIENTO AL MODAL
var modal = document.getElementById('ventana-modal')
var btnCrear = document.getElementById('btn-crear')
var btnCerrar = document.getElementById('cerrar')

btnCrear.addEventListener('click', function () {
    modal.style.display = 'block'
})

btnCerrar.addEventListener('click', function () {
    modal.style.display = 'none'
})


//VALIDACION DEL FORM

// VALIDAR DUEÑO

function validarEnvio (event){
    event.preventDefault();
    
    if ($('#dueño').val().trim() === '') {
        alert('el campo dueño esta vacio')
        $('#dueño').css({'border': '2px solid red'})
        return false
    }

    if ($('#direccion').val().trim() == '') {
        alert('el campo direccion esta vacio')
        $('#direccion').css({'border': '2px solid red'})
        return false
    }

    if ($('#localidad').val().trim() == '') {
        alert('el campo localidad esta vacio')
        $('#localidad').css({'border': '2px solid red'})
        return false
    }

    if ($('#propiedad').val().trim() == '') {
        alert('el campo propiedad esta vacio')
        $('#propiedad').css({'border': '2px solid red'})
        return false
    }

    if ($('#tipo').val().trim() == '') {
        alert('el campo tipo esta vacio')
        $('#tipo').css({'border': '2px solid red'})
        return false
    }

    if ($('#precio').val().trim() == '') {
        alert('el campo precio esta vacio')
        $('#precio').css({'border': '2px solid red'})
        return false
    }

    if ($('#descripcion').val().trim() == '') {
        alert('el campo descripcion esta vacio')
        $('#descripcion').css({'border': '2px solid red'})
        return false
    }

    $('#ventana-modal').css('display', 'none');
    this.reset();
}

$('#formulario').submit(validarEnvio);