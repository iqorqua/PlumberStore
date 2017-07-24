$(function() {
  new WOW().init();
  $('#fullpage').fullpage({
    // WOWはスクロールイベントを感知しているので、scrollBar:trueにする必要がある
    scrollBar:true
  });
});