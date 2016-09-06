$(function() {

function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}

var cardlist = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.whitespace,
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  // url points to a json file that contains an array of country names, see
  // https://github.com/twitter/typeahead.js/blob/gh-pages/data/countries.json
  prefetch: '/cardlist'
});

// passing in `null` for the `options` arguments will result in the default
// options being used
$('#cardname').typeahead(null, {
  name: 'cardlist',
  source: cardlist
});


$("#add").click(function(){
	var cardname = $('#cardname').val();
	$.getJSON("/cardinfo/" + cardname, function(result){
       		if (isEmpty(result)){
			alert('Card does not exist');
		}
		else
		{
			var cardqty = $('#qty').val();
			$("#cardlist").append(cardname + ' x' + cardqty + '<br />');
		}
		
        });
    
});




});