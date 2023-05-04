
 // Populate with proper value for size and quantity while loading the page  
window.onload = function(){
    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty-input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var sku = $(allQtyInputs[i]).attr('data-sku');
        handleEnableDisable(sku);
    }
};


//  Disable +/- buttons ouside the range 1 - available quantity for both destop 
//  and smaller screen
function handleEnableDisable(sku){       
    var currentValue = parseInt($(`#id_qty_${sku}`).val());
    var maxValue = parseInt(parseInt($('.qty-input').attr('max')));
    var minusDisable = currentValue < 2 ;
    var plusDisable = currentValue > maxValue-1;
    // mobile view
    $(`#mob-decrement-qty-${sku}`).prop('disabled', minusDisable);
    $(`#mob-increment-qty-${sku}`).prop('disabled', plusDisable);
    // desktop view
    $(`#decrement-qty-${sku}`).prop('disabled', minusDisable);
    $(`#increment-qty-${sku}`).prop('disabled', plusDisable);     
}
    
// Desktop decrement product quatity 
$('.decrement-qty').click(function(e){
    e.preventDefault();
    var currentPos = $(this).closest('.input-group').find('.qty-input')[0];
    var sku = $('.qty-input').attr('data-sku');
    var currentValue = parseInt($(currentPos).val());
    if( currentValue >1 ){
        $(currentPos).val(currentValue-1);
    }
    handleEnableDisable(sku);  
    var form = $(this).closest('.update-form')[0];
    form.submit();    
});

// Desktop increment product quantity
$('.increment-qty').click(function(e){      
    var sku = $('.qty-input').attr('data-sku');
    e.preventDefault();
    var currentPos = $(this).closest('.input-group').find('.qty-input')[0];
    var currentValue = parseInt($(currentPos).val());

    if(currentValue < parseInt($(currentPos).attr('max'))){
        $(currentPos).val(currentValue+1);
    }
    handleEnableDisable(sku);
    var form = $(this).closest('.update-form')[0];
    form.submit();    
});

//Mobile  Decrement product quatity 
$('.mob-decrement-qty').click(function(e){
    e.preventDefault();
    var currentPos = $(this).closest('.input-group').find('.qty-input')[0];
    var sku = $('.qty-input').attr('data-sku');
    var currentValue = parseInt($(currentPos).val());
    if( currentValue >1 ){
        $(currentPos).val(currentValue-1);
    }
    handleEnableDisable(sku);  
    var form = $(this).closest('.update-form')[0];
    form.submit();    
});

// Mobile Increment product quantity
$('.mob-increment-qty').click(function(e){      
    var sku = $('.qty-input').attr('data-sku');
    e.preventDefault();
    var currentPos = $(this).closest('.input-group').find('.qty-input')[0];
    var currentValue = parseInt($(currentPos).val());
    if(currentValue < parseInt($(currentPos).attr('max'))){
        $(currentPos).val(currentValue+1);
    }
    handleEnableDisable(sku);
    var form = $(this).closest('.update-form')[0];
    form.submit();    
});

// remove an item from the shopping bag
$('.remove-link').click(function(e){
    var csrfToken = "{{csrf_token}}";
    var size = $(this).data('product_size');
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/bag/remove/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': csrfToken,
        'product_size': size,
    };
    $.post(url,data).done(function(){
        location.reload();
    });
});

// float button
$('.btt-link').click(function(e) {
        window.scrollTo(0,0);
});
