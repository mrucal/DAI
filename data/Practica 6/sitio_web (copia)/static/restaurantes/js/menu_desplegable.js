var m1_leave = false;
var sm1_leave = false;
$(function(){
	$('#m1').mouseover(function(){

		sm1_leave = true;
		$('#m1').css({'margin-bottom':'0'});
		$('#sm1').slideDown(1000);
		m1_leave = false;
	});
});

$(function(){
	$('#m1').mouseleave(function(){
		setTimeout ("if (m1_leave == false){$('#sm1').slideUp(1000);}",50); 
	});
});

$(function(){
	$('#sm1').mouseover(function(){
		m1_leave = true;
		$('#sm1').css({'display':'line'});
		sm1_leave = false;
	});

});

$(function(){
	$('#sm1').mouseleave(function(){
		setTimeout ("if (sm1_leave == false){$('#sm1').slideUp(1000);}",50); 
	});
});

/*****************************************************************/

var m2_leave = false;
var sm2_leave = false;
$(function(){
	$('#m2').mouseover(function(){

		sm2_leave = true;
		$('#m2').css({'margin-bottom':'0'});
		$('#sm2').fadeIn(1000);
		m2_leave = false;
	});
});

$(function(){
	$('#m2').mouseleave(function(){
		setTimeout ("if (m2_leave == false){$('#sm2').fadeOut(1000);}",50); 
	});
});

$(function(){
	$('#sm2').mouseover(function(){
		m2_leave = true;
		$('#sm2').css({'display':'line'});
		sm2_leave = false;
	});

});

$(function(){
	$('#sm2').mouseleave(function(){
		setTimeout ("if (sm2_leave == false){$('#sm2').fadeOut(1000);}",50); 
	});
});

/*****************************************************************/

var m3_leave = false;
var sm3_leave = false;
$(function(){
	$('#m3').mouseover(function(){

		sm3_leave = true;
		$('#m3').css({'margin-bottom':'0'});
		$('#sm3').slideDown(1000);
		m3_leave = false;
	});
});

$(function(){
	$('#m3').mouseleave(function(){
		setTimeout ("if (m3_leave == false){$('#sm3').slideUp(1000);}",50); 
	});
});

$(function(){
	$('#sm3').mouseover(function(){
		m3_leave = true;
		$('#sm3').css({'display':'line'});
		sm3_leave = false;
	});

});

$(function(){
	$('#sm3').mouseleave(function(){
		setTimeout ("if (sm3_leave == false){$('#sm3').slideUp(1000);}",50); 
	});
});

/*****************************************************************/

var colores = 0;

$(function(){
	$('#color-boton').click(function(){
		colores = (colores + 1) % 3;
		console.log('BREAK');
		switch(colores){
			case 0:
				$('.first_color').css({'background-color': 'black'});
				$('.second_color').css({'background-color': '#eeeeee'});
				$('.first_color_ico').css({'color': 'black'});
				$('.second_color_ico').css({'color': '#eeeeee'});
				break;
			case 1:
				$('.first_color').css({'background-color': '#860e21'});
				$('.second_color').css({'background-color': '#e7bb94'});
				$('.first_color_ico').css({'color': '#860e21'});
				$('.second_color_ico').css({'color': '#e7bb94'});
				break;
			case 2:
				$('.first_color').css({'background-color': '#4028ee'});
				$('.second_color').css({'background-color': '#9ce8ae'});
				$('.first_color_ico').css({'color': '#4028ee'});
				$('.second_color_ico').css({'color': '#9ce8ae'});
				break;

		}
	});
});

var fuentes = 0;

$(function(){
	$('#letra-boton').click(function(){
		fuentes = (fuentes + 1) % 2;
		console.log('BREAK');
		switch(fuentes){
			case 0:
				$('.first_color_txt').css({'color': 'black'});
				$('.second_color_txt').css({'color': 'white'});
				$('.tipo_fuente').css({'font-family':'Arial,Helvetica Neue,Helvetica,sans-serif'});
				break;
			case 1:
				$('.first_color_txt').css({'color': 'blue'});
				$('.second_color_txt').css({'color': 'green'});
				$('.tipo_fuente').css({'font-family':'Vegur, "Times New Roman", Times, serif'});
				break;

		}
	});
});

