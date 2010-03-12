jQuery(function(){
  /*jQuery('#projects-list').tabs("#projects-list ul", {
    tabs: 'h2',
    effect: 'slide'				
  });*/
  
  jQuery("ul.tabs").tabs("ul.panes >li", {
    effect: 'fade'
  });
})
