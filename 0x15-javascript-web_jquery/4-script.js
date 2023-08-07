$('DIV#toggle_header').click(function () {
  if ($('header').attr('class') === 'red') {
    $('header').attr('class', 'green');
  } else if ($('header').attr('class') === 'green') {
    $('header').attr('class', 'red');
  }
});
