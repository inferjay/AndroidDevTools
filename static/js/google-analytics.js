/*
* @Author: inferjay
* @Date:   2016-03-26 17:47:29
* @Last Modified by:   inferjay
* @Last Modified time: 2024-04-09 13:16:21
*/
window.dataLayer = window.dataLayer || [];
function gtag() { dataLayer.push(arguments); }
gtag('js', new Date());

gtag('config', 'G-NQH6H0E3Y6');
var trackOutboundLink = function (url, category, action) {
    var redirectTriggered = false;
    gtag('send', 'event', category, action, url, {
        'hitCallback': function () {
            redirectTriggered = false;
            window.open(url, '_blank');
        }
    });
};