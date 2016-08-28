$(function() {
	var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        autoplay: 4000,
        autoplayDisableOnInteraction: false,
        speed: 600,
        slidesPerView: 1,
        loop: true,

    });
})