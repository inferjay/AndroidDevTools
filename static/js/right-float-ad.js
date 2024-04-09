let rightAdContainer = $('#auto-scroll-ad-box');
let rightAds = [
    {
        "title": "短期暴力提升，快速突破瓶颈。HenCoder Plus 作为一套全方位系统化的高级进阶课程，开课四期以来，吸纳了来自阿里、腾讯、百度、头条、滴滴等公司以及硅谷、台湾和日本的众多学员报名参加，多位学员在毕业一个月内先后入职阿里、腾讯、小米、头条等公司。学员年薪最高达到 80w，多位学员年薪达到 45w 左右。",
        "link": "https://plus.hencoder.com",
        "image": "https://i.loli.net/2019/05/23/5ce663bb003ec62326.gif",
        "ad_tag": "AD-HenCoderPlus",
        "isshow": true,
        "start_time": "2019-3-30 00:30:00",
        "end_time": "2021-8-5 00:00:00"
    },
    {
        "title": "",
        "link": "https://www.ucloud.cn/site/global.html?ytag=androiddevtools",
        "image": "https://i.loli.net/2020/05/15/DOv28AnZ73qfmiE.png",
        "ad_tag": "AD-UCloud",
        "isshow": true,
        "start_time": "2020-1-1 00:00",
        "end_time": "2021-5-15 00:00"
    }
];
rightAds.filter(isShow).filter(isExpired).forEach((item) => {
    let { title, link, ad_tag, image } = item;
    let adElement = `<div class="ad-float-right"><a href="${link}" title="${title}" onclick="trackOutboundLink('${link}', '${ad_tag}', 'click');" target="_blank"><img src="${image}"></a></div>`;
    rightAdContainer.append(adElement);
});