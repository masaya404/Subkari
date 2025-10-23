console.log("loaded");

// $(document).on('submit', '#loginForm', function(e) {
//   e.preventDefault();
//   console.log("submit handler triggered!");
// });

$(document).ready(function() {
  $('#loginForm').on('submit', function(e) {
    e.preventDefault(); 
    console.log("form submitted via AJAX");

    //エラーメッセージ削除
    $('.error-text').text('');
    $('input').removeClass('input-error');

    $.ajax({
      url: $(this).attr('action'),
      type: 'POST',
      data: $(this).serialize(), // 
      dataType: 'json',
      success: function(response) {
        console.log("AJAX success:", response);
        if (!response.success) {
          // 
          if (response.errors.mail) {
            $('#mail').addClass('input-error');
            $('#mailError').text(response.errors.mail);
          }
          if (response.errors.password) {
            $('#password').addClass('input-error');
            $('#passwordError').text(response.errors.password);
          }
        } else {
          // 成功 
          window.location.href = response.redirect;
        }
      },
      error: function() {
        console.log("AJAX error:", xhr.responseText);
        alert('通信エラーが発生しました。もう一度お試しください。');
      }
    });
  });
});

