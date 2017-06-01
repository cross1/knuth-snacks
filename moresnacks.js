$(document).ready(function() {
  $('#button').click(function(){
    var newItem = $('input[name=snack-suggestion]').val();
    $('.list-of-snacks').append('<div class="newItem">' + newItem +'</div>');
  });
});
