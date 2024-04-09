//bind a click
var utm_info = "utm_source=androiddevtools&utm_medium=website";
$(document).bind("MutationObserver", function (event) {
  $('a[href^="http"]').each(function () {
    if (!$(this).attr("target")) {
      $(this).attr("target", "_blank");
    }
    var url = $(this).attr("href");
    if (url.indexOf("androiddevtools.cn") != -1) {
      $(this).attr("target", "_self");
    } else {
      if (url && url.indexOf(utm_info) == -1) {
        if (url.indexOf("?") == -1) {
          url += "?";
        } else {
          url += "&";
        }
        url += utm_info;
        $(this).attr("href", url);
      }
    }
  });
});
