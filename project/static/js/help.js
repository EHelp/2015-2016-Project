$(function() {
	$('.users-center li').click(function() {
		$('.users-center li').removeClass('active');
		var temp = $(this).attr('class');
		$(this).addClass('active');
		$('.center-content p').hide();
		$('.' + temp).show();
	})

})