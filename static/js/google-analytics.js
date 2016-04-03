/*
* @Author: inferjay
* @Date:   2016-03-26 17:47:29
* @Last Modified by:   inferjay
* @Last Modified time: 2016-04-03 14:59:00
*/
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-52369435-2', 'auto');
ga('send', 'pageview');
var trackOutboundLink = function(url,category, action) {
    var redirectTriggered = false;
    ga('send', 'event', category, action, url, {'hitCallback':
        function() {
            redirectTriggered = true;
            window.open(url);
        }
    });
    setTimeout(function() {
        if (!redirectTriggered) {
            window.open(url);
        }
    }, 200);
};