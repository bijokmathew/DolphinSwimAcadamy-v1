let country_selected = $('#id_default_country').val
console.log('country_selected', country_selected)
if (!country_selected){
    $('#id_default_country').css('color', '#aab7c4')
} 
$('#id_default_country').change(function(){
    country_selected = $(this).val();
    if(!country_selected){
        $(this).css('color', '#aab7c4')
    } else {
        $(this).css('color', '#000')
    }

});