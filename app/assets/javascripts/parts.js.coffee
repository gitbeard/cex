# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://jashkenas.github.com/coffee-script/

#show = (id) -> document.getElementById(id).style.visibility = 'visible';


$ ->
  
  $('span#alt_item_number').show()
  $('span#item_number').hide()
  $('span#ca_inv').hide()
  $('span#nc_inv').hide()
  $('span#wip').hide()
  $('span#transit').hide()
  
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
      $('span#ca_inv').show()
    else
      $('span#ca_inv').hide()
    
    if($("#cd").is(":checked"))
      $('span#nc_inv').show()
    else
      $('span#nc_inv').hide()
    
    if($("#ce").is(":checked"))
      $('span#wip').show()
    else
      $('span#wip').hide()
      
    if($("#cf").is(":checked"))
      $('span#transit').show()
    else
      $('span#transit').hide()
      
  $("#test").click(change)
