// Source: http://bootsnipp.com/snippets/featured/bootstrap-lightbox
$(document).ready(function() {
  var $lightbox = $('#lightbox');
  
  $('[data-target="#lightbox"]').on('click', function(event) {
      var $img = $(this).find('img'), 
          src = $img.attr('src'),
          alt = $img.attr('alt')
          ;

      $lightbox.find('img').attr('src', src);
      $lightbox.find('img').attr('alt', alt);
  });
  
  $lightbox.on('shown.bs.modal', function (e) {
      var $img = $lightbox.find('img');
  });
});	