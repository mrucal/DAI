var tabla_original;
var paginador_original;
var numFilas = 8;
var numPaginas;
var pagActual = 1;
$(document).ready(function() { 
	tabla_original = $("#customers").clone();
	paginador_original = $(".pagination").clone();

});



$(function() {
	$("#myform").submit(function(e) {
		$('#tabla_restaurantes').css({'display':'block'});
		enviar_post(e,0,1);
	   });
});

var enviar_post = function(e, primeraFila, nuevaPagActual){

			e.preventDefault();
			       
			var actionurl = e.currentTarget.action;

			pagActual = nuevaPagActual;

			$.ajax({
			    url: actionurl,
			    type: 'post',
			    data: $("#myform").serialize()+'&pag_actual='+ pagActual, 
			    success: function(data) {
				    
				    // Crear tabla html
				    numPaginas = Math.round(data[0].length / numFilas);
				    console.log('BREAKPOST4 '+numPaginas+' '+numFilas+' pagActual: '+pagActual);
				    crear_pagina(data,primeraFila);
				    // Añadir total de restaurantes en encabezado de la tabla
				    $('#total').append('('+data[0].length+' en total)');
				    // Añadir opcion elegida
				    $("#opcion_elegida").text(data[1]);
				    // Añadir encabezado para la columna de tipo de cocina
				    if(data[2] == 'true')
				    	$('#tr_id').append("<th class='first_color second_color_txt tipo_fuente' style='width:25%'>Tipo Cocina</th>");

				    $('#pagPrimera').click(function(){

						enviar_post(e,0,1);

					});
				    $('#pagAnt').click(function(){

						enviar_post(e,(pagActual-2)*numFilas,pagActual-1);

					});
					for (var i = 1; i <= numPaginas; i++) {
						$('#pag'+i).click(function(){

							var nPag = obtener_num_pag($(this).attr("id"));

							console.log('BREAK '+(nPag-1)*numFilas+' PAG_actual: '+nPag);

							enviar_post(e,(nPag-1)*numFilas,nPag);

						});
					}
					$('#pagSig').click(function(){

						enviar_post(e,(pagActual)*numFilas,pagActual+1);

					});
					$('#pagUltima').click(function(){

						enviar_post(e,(numPaginas-1)*numFilas,numPaginas);

					});
			   	}
			});
}


var crear_pagina = function(data,filaInicial){
					// Restaurar la tabla original para evitar que se añadan etiquetas a busquedas anteriores
				    $("#customers").replaceWith(tabla_original.clone());
					var contenido = '';
				    for (var i = filaInicial; i < filaInicial+numFilas && i < data[0].length; i++) {
				     	contenido += '<tr><td class="first_color_txt tipo_fuente">' + data[0][i].nombre + '</td>';
				     	if(data[2] == 'true'){
				    	    contenido += '<td class="first_color_txt tipo_fuente">' + data[0][i].direccion + '</td>';
				    	    contenido += '<td class="first_color_txt tipo_fuente">' + data[0][i].cocina + '</td></tr>';
				    	}else{
				    		contenido += '<td class="first_color_txt tipo_fuente">' + data[0][i].direccion + '</td></tr>';
				    	}
				    }
				    paginacion='';
				    var pu_pag = obtener_primera_ultima_pagina(pagActual,numPaginas);
				    console.log(pu_pag+' '+pagActual+'numPaginas: '+numPaginas);
				    if(pagActual>1){
				    	paginacion += '<li ><input id="pagPrimera" class="pagina btn btn-default second_color  first_color_txt tipo_fuente" type = "submit" value="&laquo;"></li>'
				    	paginacion += '<li ><input id="pagAnt" class="pagina btn btn-default second_color  first_color_txt tipo_fuente" type = "submit" value="&lt;"></li>'
				    }
				    if (pu_pag[5])
				    	paginacion += '<li ><input id="pag'+(pu_pag[0]-50)+'" class="pagina btn btn-default second_color  first_color_txt tipo_fuente" type = "submit" value="'+(pu_pag[0]-50)+'"></li>'
				    if (pu_pag[3])
				    	paginacion += '<li ><input id="pag'+(pu_pag[0]-10)+'" class="pagina btn btn-default second_color  first_color_txt tipo_fuente" type = "submit" value="'+(pu_pag[0]-10)+'"></li>'
				    for (var i = pu_pag[0]; i <= pu_pag[1]; i++){
				    	//<li><a href="#">&laquo;</a></li>
				    	//paginacion += '<li id="pag'+i+'"><a href="#">'+i+'</a></li>'
				    	if (i==pagActual)
				    		paginacion += '<li ><input id="pag'+i+'" class="pagina btn btn-default first_color  second_color_txt tipo_fuente"  type = "submit" value="'+i+'"></li>'
				    	else
				    		paginacion += '<li ><input id="pag'+i+'" class="pagina btn btn-default second_color  first_color_txt tipo_fuente" type = "submit" value="'+i+'"></li>'

				    }			
				     if (pu_pag[2])
				    	paginacion += '<li ><input id="pag'+(pu_pag[1]+10)+'" class="pagina btn btn-default second_color  first_color_txt tipo_fuente" type = "submit" value="'+(pu_pag[1]+10)+'"></li>'	    
				    if (pu_pag[4])
				    	paginacion += '<li ><input id="pag'+(pu_pag[1]+50)+'" class="pagina btn btn-default second_color  first_color_txt tipo_fuente" type = "submit" value="'+(pu_pag[1]+50)+'"></li>'
				   	if(pagActual<numPaginas){
				    	paginacion += '<li ><input id="pagSig" class="pagina btn btn-default second_color  first_color_txt tipo_fuente" type = "submit" value="&gt;"></li>'
				    	paginacion += '<li ><input id="pagUltima" class="pagina btn btn-default second_color  first_color_txt tipo_fuente" type = "submit" value="&raquo;"></li>'
				    }
				    $(".pagination").replaceWith(paginador_original.clone());
				    $('.pagination').append(paginacion);

				    //console.log(paginacion);
				    // Añadir tabla
				    $('#customers').append(contenido);
};



var obtener_num_pag = function(id){
	var nPag = 1;
	if (id.length == 4)
		nPag = Number(id[3]);
	if (id.length == 5)
		nPag = Number(id[3])*10 + Number(id[4]);
	if (id.length == 6)
		nPag = Number(id[3])*100 + Number(id[4])*10 + Number(id[5]);
	if (id.length == 7)
		nPag = Number(id[3])*1000 + Number(id[4])*100 + Number(id[5])*10 + Number(id[6]);

	console.log('Nummero de pagina: '+nPag);
	return nPag;
}

var obtener_primera_ultima_pagina = function(actual,total){

	var primera = 1;
	var ultima = total;
	var mas10 = false;
	var menos10 = false;
	var mas50 = false;
	var menos50 = false;

	console.log('obtener '+primera+' '+ultima+' '+actual+' '+total);
	if (actual <= total - 2)
		ultima = actual + 2;
	if (actual > 2)
		primera = actual - 2;
	else
		if(total>5)
			ultima = 3;
	
	if (ultima+10 <= total)
		mas10 = true;
	if (primera-10 >= 1)
		menos10 = true;
	if (ultima+50 <= total)
		mas50 = true;
	if (primera-50 >= 1)
		menos50 = true;

	console.log('obtener2 '+primera+' '+ultima+' '+actual+' '+total+' '+mas10+' '+menos10+' '+mas50+' '+menos50);

	return [primera,ultima,mas10,menos10,mas50,menos50];
}