jQuery(function(){
  var lightboxOptions = {
    fixedNavigation: true,
    imageLoading: '/s/image/lightbox/lightbox-ico-loading.gif',
		imageBtnPrev: '/s/image/lightbox/lightbox-btn-prev.gif',
		imageBtnNext: '/s/image/lightbox/lightbox-btn-next.gif',
		imageBtnClose: '/s/image/lightbox/lightbox-btn-close.gif',
		imageBlank: '/s/image/lightbox/lightbox-blank.gif'
  };
  jQuery('.photos a').lightBox(lightboxOptions);
  /*jQuery('#projects-list').tabs("#projects-list ul", {
    tabs: 'h2',
    effect: 'slide'
  });*/
});
