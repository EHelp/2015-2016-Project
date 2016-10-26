$(document).ready(function(){
	$('.show-inform0').bind("click",function(){
		var elem = $(this);
		if(elem.data('flipped'))
		{
			elem.revertFlip();
			elem.data('flipped',false)
		} else {
			elem.flip({
				direction:'lr',
				speed: 350,
				onBefore: function(){
					elem.html(elem.siblings('.hide-inform0').html());
				}
			});
			elem.data('flipped',true);
		}
	});
	$('.show-inform1').bind("click",function(){
		var elem = $(this);
		if(elem.data('flipped'))
		{
			elem.revertFlip();
			elem.data('flipped',false)
		} else {
			elem.flip({
				direction:'lr',
				speed: 350,
				onBefore: function(){
					elem.html(elem.siblings('.hide-inform1').html());
				}
			});
			elem.data('flipped',true);
		}
	});
	$('.show-inform2').bind("click",function(){
		var elem = $(this);
		if(elem.data('flipped'))
		{
			elem.revertFlip();
			elem.data('flipped',false)
		} else {
			elem.flip({
				direction:'lr',
				speed: 350,
				onBefore: function(){
					elem.html(elem.siblings('.hide-inform2').html());
				}
			});
			elem.data('flipped',true);
		}
	});


	//next pointer
	$(".to-intro0").bind("click", function() {
		$('body,html').animate({scrollTop:1300},1000);
	});
	$(".to-intro1").bind("click", function() {
		$('body,html').animate({scrollTop:2300},1000);
	});
	$(".to-intro2").bind("click", function() {
		$('body,html').animate({scrollTop:3320},1000);
	});
	$(".to-intro3").bind("click", function() {
		$('body,html').animate({scrollTop:4370},1000);
	});
	$(".to-intro4").bind("click", function() {
		$('body,html').animate({scrollTop:5300},1000);
	});
});
























$(function() {

	$(window).scroll(function() {
		$(".test").html($(window).scrollTop()+ " px");
		if ($(window).scrollTop() > 100 && $(window).scrollTop() < 1400) {
			$(".image0").css("background-position", "50% " + (10 - $(window).scrollTop()*0.03) +"px");
		}
		if ($(window).scrollTop() > 1200 && $(window).scrollTop() < 2500) {
			$(".image1").css("background-position", "50% " + (10 - $(window).scrollTop()*0.03) +"px");
		}
		if ($(window).scrollTop() > 2100 && $(window).scrollTop() < 3400) {
			$(".image2").css("background-position", "50% " + (10 - $(window).scrollTop()*0.03) +"px");
		}
		if ($(window).scrollTop() > 3100 && $(window).scrollTop() < 4400) {
			$(".image3").css("background-position", "50% " + (10 - $(window).scrollTop()*0.03) +"px");
		}
		if ($(window).scrollTop() > 4100) {
			$(".image4").css("background-position", "50% " + (10 - $(window).scrollTop()*0.03) +"px");
		}
	});






	/*
	var flag = 1;
	$('.show-inform').bind("mouseover",function(){
		var elem = $(this);
		if (flag == 1) {
			elem.flip({
				direction:'lr',
				speed: 350,
				onBefore: function(){
					elem.html(elem.siblings('.hide-inform').html());
				}
			});
			flag = 2;
		}
	});
	$('.show-inform').bind("mouseout",function(){
		flag = 1;
		var elem = $(this);
		if (flag == 1) {
			elem.flip({
				direction:'lr',
				speed: 350,
				onBefore: function(){
					elem.html(elem.siblings('.hide-inform').html());
				}
			});
			flag = 2;
		}
	});
*/
});






