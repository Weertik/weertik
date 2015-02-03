
/* Background Images
-------------------------------------------------------------------*/
var  pageTopImage = jQuery('#page-top').data('background-image');
var  aboutImage = jQuery('#about').data('background-image');
var  subscribeImage = jQuery('#subscribe').data('background-image');
var  contactImage = jQuery('#contact').data('background-image');

if (pageTopImage) {  jQuery('#page-top').css({ 'background-image':'url(' + pageTopImage + ')' }); };
if (aboutImage) {  jQuery('#about').css({ 'background-image':'url(' + aboutImage + ')' }); };
if (subscribeImage) {  jQuery('#subscribe').css({ 'background-image':'url(' + subscribeImage + ')' }); };
if (contactImage) {  jQuery('#contact').css({ 'background-image':'url(' + contactImage + ')' }); };

/* Background Images End
-------------------------------------------------------------------*/

/* Window Height Resize--------------------------------------------*/
function resize(){
    windowHeight = 440
    nowWindowHeight = window.innerHeight
    if(nowWindowHeight >= 440){
        nowWindowHeight = window.innerHeight
    }
    document.getElementById('page-top').style.height = nowWindowHeight + 'px';
    document.getElementById('pattern').style.height = nowWindowHeight + 'px';
}
/* Window Height Resize End
-------------------------------------------------------------------*/

/* Document Ready function
-------------------------------------------------------------------*/
jQuery(document).ready(function($) {
    resize()
    window.addEventListener("resize", resize);
});

/* Document Ready function End
-------------------------------------------------------------------*/

/* Preloder
-------------------------------------------------------------------*/
$(window).load(function () {
    "use strict";
    $("#loader").fadeOut();
    $("#preloader").delay(350).fadeOut("slow");
});
 /* Preloder End
-------------------------------------------------------------------*/
