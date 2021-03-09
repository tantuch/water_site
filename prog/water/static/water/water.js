// can't loads the file, see 
// https://stackoverflow.com/questions/62604990/getting-uncaught-referenceerror-is-not-defined-for-jquery
// var $ = globalThis.jQuery
var onProducts= function() {
	$("#products").css("padding-top", "180px");
	$("#products").css("margin-top", "0px");
};
var onMain = function() {
	$("#products").css("padding-top", "0px");
	$("#products").css("margin-top", "220px");
};
