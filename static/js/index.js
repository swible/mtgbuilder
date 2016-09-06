$(function() {

var cardlist = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.whitespace,
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  // url points to a json file that contains an array of country names, see
  // https://github.com/twitter/typeahead.js/blob/gh-pages/data/countries.json
  prefetch: '/cardlist'
});

// passing in `null` for the `options` arguments will result in the default
// options being used
$('#usr').typeahead(null, {
  name: 'cardlist',
  source: cardlist
});


$("#add").click(function(){
	//check if card exists
	//if it does add to assoc array
	//then add to list
    $("#cardlist").append("Some appended text.");
});


});