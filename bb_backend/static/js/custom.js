price_changed = false
$('#sel1').on('change', function () {
	buildurl()
})

$('.optradio').click(function(){
    var selectedOption = $("input:radio[name=optradio]:checked").val()
	buildurl()
})

$('.pricerange').change(function(){
    var price = $(this).val();
    price_changed = true;
    buildurl()
});

$(function() {
  
  $('.colourbox').click(function() {
    buildurl()
  });
});
function search(){
	buildurl()
}

function buildurl(){
	var search = document.getElementById('searchbox').value;
	var current_url = window.location.href
	var clean_url = current_url.substring(0, current_url.indexOf("?"));
	var brand_name = $('#sel1').val()
	var sl_type = $("input:radio[name=optradio]:checked").val()
	if(sl_type==undefined) {
		sl_type=""

	}
	var sl_price = $('.pricerange').val()
    var colours = [];
    $('.checkbox input[type="checkbox"]:checked').each(function() {
      colours.push($(this).val());
    });
    var qm = false
    if (search){
    	if (qm==false){
    		console.log("1")
    	var clean_url = clean_url+"?search="+search
    	qm=true
       	}
	}
    
    if (brand_name){
    	console.log("2")
    	if (qm==true){
    		var clean_url = clean_url+"&brand_name="+brand_name
    	}
    	else {
    		var clean_url = clean_url+"?brand_name="+brand_name
    		qm=true
    	}
    }
    if (sl_type){
    	console.log("3")
    	if (qm==true){
    		var clean_url = clean_url+"&sl_type="+sl_type
    	}
    	else{
    		var clean_url = clean_url+"?sl_type="+sl_type
    		qm=true
    	}
    }
    if (sl_price && price_changed){
    	price_changed = false
    	console.log("4")
    	if (qm==true){
    		console.log("ooooo")
    	var clean_url = clean_url+"&sl_price="+sl_price
		}
		else{
			console.log("uu")
			var clean_url = clean_url+"?sl_price="+sl_price
			qm=true
		}	
    }
    if (colours.length > 0){
    	console.log("5")
    	console.log(colours)
    	if (qm==true){
    		var clean_url = clean_url+"&colours="+colours
    	}
    	else{
    		var clean_url = clean_url+"?colours="+colours
    	}
    }
	window.location = clean_url
}