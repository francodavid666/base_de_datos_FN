//COLORES DEL ESTADO
$('td:contains("disponible")').css('color', 'blue')
$('td:contains("alquilado")').css('color', 'red')
$('td:contains("en alquiler")').css('color', 'green')
$('td:contains("en venta")').css('color', 'green')
$('td:contains("por vender")').css('color', 'orange')
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

if ($('td:contains("por vender")')) {
    $('td:contains("por vender")').html('<div class="punto-naranja"></div>por vender')
}

if ($('td:contains("vendido")')) {
    $('td:contains("vendido")').html('<div class="punto-rojo"></div>vendido')
}


