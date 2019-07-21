var tabla_original;
$(document).ready(function() { 
	tabla_original = $("#customers").clone();
});

$(function(){
	$('#restaurante-boton').click(function(){
		$('#tabla_restaurantes').css({'display':'block'});
	});

	$(function() {
		$("#myform").submit(function(e) {

			e.preventDefault();
			       
			var actionurl = e.currentTarget.action;

			$.ajax({
			    url: actionurl,
			    type: 'post',
			    data: $("#myform").serialize(),
			    success: function(data) {
				    // Restaurar la tabla original para evitar que se añadan etiquetas a busquedas anteriores
				    $("#customers").replaceWith(tabla_original.clone());
				    // Crear tabla html
				    var contenido = '';
				    for (var i = 0; i < data[0].length; i++) {
				     	contenido += '<tr><td class="first_color_txt tipo_fuente">' + data[0][i].nombre + '</td>';
				     	if(data[2] == 'true'){
				    	    contenido += '<td class="first_color_txt tipo_fuente">' + data[0][i].direccion + '</td>';
				    	    contenido += '<td class="first_color_txt tipo_fuente">' + data[0][i].cocina + '</td></tr>';
				    	}else{
				    		contenido += '<td class="first_color_txt tipo_fuente">' + data[0][i].direccion + '</td></tr>';
				    	}
				    }
				    // Añadir tabla
				    $('#customers').append(contenido);
				    // Añadir total de restaurantes en encabezado de la tabla
				    $('#total').append('('+data[0].length+' en total)');
				    // Añadir opcion elegida
				    $("#opcion_elegida").text(data[1]);
				    // Añadir encabezado para la columna de tipo de cocina
				    if(data[2] == 'true')
				    	$('#tr_id').append("<th class='first_color second_color_txt tipo_fuente' style='width:25%'>Tipo Cocina</th>");
				    	
			   	}
			});

	    });

	});

});