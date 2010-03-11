jQuery(function(){
  var lightboxOptions = {
    fixedNavigation: true,
    imageLoading: '/s/image/lightbox/lightbox-ico-loading.gif',
		imageBtnPrev: '/s/image/lightbox/lightbox-btn-prev.gif',
		imageBtnNext: '/s/image/lightbox/lightbox-btn-next.gif',
		imageBtnClose: '/s/image/lightbox/lightbox-btn-close.gif',
		imageBlank: '/s/image/lightbox/lightbox-blank.gif'
  };
  jQuery('img.advancedpanorama').panorama({
    auto_start: 0,
    start_position: 1527
  });
  jQuery("ul.tabs").tabs("ul.panes >li", {
    effect: 'fade'
  });
  jQuery('.photos a, #project-photo').lightBox(lightboxOptions);
});
