$(function() {
	var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        paginationClickable: true,
        slidesPerView: 'auto',
        initialSlide: 3,
        coverflow: {
            rotate: 50,
            strech: 0,
            depth: 100,
            modifier: 1,
            slideShadows: true
        }
    });
})