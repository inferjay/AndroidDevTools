var lastScrollY = 0;
var initTop = 100;

function heartBeat() {
  var diffY = 0;
  if (window.pageYOffset) {
    //这一条滤去了大部分， 只留了IE678
    diffY = window.pageYOffset;
  } else if (document.documentElement.scrollTop) {
    //IE678 的非quirk模式
    diffY = document.documentElement.scrollTop;
  } else if (document.body.scrolltop) {
    //IE678 的quirk模式
    diffY = document.body.scrolltop;
  }
  var percent = 0.1 * (diffY - lastScrollY);
  if (percent > 0) {
    percent = Math.ceil(percent);
  } else {
    percent = Math.floor(percent);
  }

  var top = String(lastScrollY + initTop) + "px";
  $("#auto-scroll-ad-box").css("top", top);
  lastScrollY = lastScrollY + percent;
}
window.setInterval("heartBeat()", 1);
