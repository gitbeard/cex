# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://jashkenas.github.com/coffee-script/

#show = (id) -> document.getElementById(id).style.visibility = 'visible';


$ ->
  
  $('span#alt_item_number').show()
  $('span#item_number').hide()
  $('span#inv_quantity').hide()
  
  change = (e) ->   
    if($("#ca").is(":checked"))
      $('span#alt_item_number').show()
    else
      $('span#alt_item_number').hide()
    
    if($("#cb").is(":checked"))
      $('span#item_number').show()
    else
      $('span#item_number').hide()
    
    if($("#cc").is(":checked"))
      $('span#inv_quantity').show()
    else
      $('span#inv_quantity').hide()
    
  $("#test").click(change)
