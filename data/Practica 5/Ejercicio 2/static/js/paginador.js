/*$(function(){
	$('#restaurante-boton').click(function(){
		$('#tabla_restaurantes').css({'display':'block'});
		$.post( "", {opcion_busqueda : $("#form_busqueda").serialize() }, function( data ) {
			console.log('BREAK')
		});

	});
});*/

$(function() {
    //hang on event of form with id=myform
    $("#form_busqueda").submit(function(e) {

        //prevent Default functionality
        e.preventDefault();

        //get the action-url of the form
        var actionurl = e.currentTarget.action;

        //do your own request an handle the results
        $.ajax({
                url: actionurl,
                type: 'post',
                data: { opcion_busqueda: $("#myform").serialize()},
                success: function(data) {
                    console.log('BREAK');
                }
        });

    });

});