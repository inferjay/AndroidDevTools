let image = $('.pop-image');
let link = $('.pop-links');
let text = $('.pop-text');
let adArray = [
    {
        "title": "学生认证立享特权，课程一律 5 折",
        "link": "http://gk.link/a/10ga3?utm_source=androiddevtools.cn&utm_medium=fixed_ad",
        "image": "https://i.loli.net/2020/05/09/xpOoSrsfjMhKkad.png",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 23:59"
    },
    {
        "title": "扫码关注「Android开发技术周报」公众号",
        "link": "https://androidweekly.io?utm_source=androiddevtools.cn&utm_medium=fixed_ad",
        "image": "https://p.ipic.vip/gzthk5.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2024-12-31 23:59"
    },
    {
        "title": "大型 Android 系统重构实战",
        "link": "http://gk.link/a/11X7S",
        "image": "https://p.ipic.vip/v4fhpw.jpeg",
        "isshow": false,
        "start_time": "2023-02-16 00:00",
        "end_time": "2023-10-01 00:00"
    },
    {
        "title": "Kotlin 协程实战",
        "link": "#",
        "image": "https://static.codefuns.tech/images/common/ad/hkj5m6.jpg",
        "isshow": false,
        "start_time": "2023-02-16 00:00",
        "end_time": "2023-10-01 00:00"
    },
    {
        "title": "20 年技术老兵，独家分享 C++ 常见陷阱及避坑经验，早鸟+口令「luoge6666」到手仅 ¥58，免费试读👆",
        "link": "https://time.geekbang.org/column/intro/100051801?code=wM%2FchWta-oOE78PL6wo4tj7nwK-L0YsyUhIDMs4GUuA%3D",
        "image": "https://i.loli.net/2020/05/09/G863MdyLA7WsQjg.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2023-6-1 00:00"
    },
    {
        "title": "设计模式之美",
        "link": "https://time.geekbang.org/column/intro/100039001?code=WA3%2FyyREnVMQiNIIdtEuF9zs9AH1EqeYFsTq9E79dP4%3D",
        "image": "https://i.loli.net/2020/05/09/Liprktm5xW1M9DC.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2023-12-31 00:00"
    },
    {
        "title": "Java业务开发常见错误100例",
        "link": "https://time.geekbang.org/column/intro/100047701?code=27vqicKbAU4sE53isHbXlaBmSfFfj2%2FbhQoBpOMRbpo%3D",
        "image": "https://i.loli.net/2020/05/09/uga2AjcWUSzmCv8.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "订阅量Top1，50000+程序员的算法课堂，整个专栏会涵盖100 多个算法真实项目场景案例，作者是前Google工程师王争，相信会开启你的趣味学习算法之旅。",
        "link": "https://time.geekbang.org/column/intro/100017301?code=C0DIG6h7m4XJmsain29Nu3IGPaD81er7Xq6%2FJiFFOC0%3D",
        "image": "https://i.loli.net/2020/05/09/rGgMPbkf1E43xhj.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "如果你想认真进阶Java或者准备面试，我推荐你好好看下《Java核心技术36讲》专栏。作者从核心知识点和能力出发，精选出36道Java面试题。作者杨晓峰是前 Oracle 首席工程师，大家都知道，Java就是Oracle公司的，内部人的专栏，给你与众不同的视角。",
        "link": "https://time.geekbang.org/column/intro/100017301?code=C0DIG6h7m4XJmsain29Nu3IGPaD81er7Xq6%2FJiFFOC0%3D",
        "image": "https://i.loli.net/2020/05/09/bDtoVumxHkaciOR.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "基于最新 Python 3，通过实际场景来学习，全面讲解标准库、第三方库和机器学习库。另有一个大模块专门讲解爬虫技能，是一个入门 Python 必看的视频课程。现已有8600+用户订阅，跟着这个课程学，从零基础到入门绝对没问题。",
        "link": "https://time.geekbang.org/course/intro/100008801?code=tKqeDSeaNexuDiJO11BlWccFgJqpO67e9PsdjXivH5A%3D",
        "image": "https://i.loli.net/2020/05/09/da6qf4UNF1WPHZO.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "作为 Java 程序员，如果你不去深入理解 Java 虚拟机，那基本是与进阶加薪无缘了。这个专栏，我记得当时上线不到3天，已经有1W人订阅，异常火爆。1、Java虚拟机确实是面试大题；2、作者是郑雨迪，Oracle Labs高级研究员，专攻Graal编译器，也在研究HotSpot虚拟机项目。",
        "link": "https://time.geekbang.org/column/intro/100010301?code=8G6pg79pz4j47n5YiavleP6AIiV6QhVzxDRk3Y8KqtU%3D",
        "image": "https://i.loli.net/2020/05/09/9Unv4Cmwhj73O2e.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "批量爬虫企业数据，违法吗？搬运其他网站的用户评论到自家平台，侵权吗？开源代码的版权，到底怎么看？转正申请不被批，劳动合同你看懂了吗？无故被裁员，工资社保跟谁要？租房碰上黑中介，维权从哪儿入手？资深律师老周为程序员量身定制，选取了职场、技术、生活三个领域中与程序员联系最密切的 40 个法律问题，给到你最实用有效的处理办法。",
        "link": "https://time.geekbang.org/column/intro/100020001?code=tkVmTFNhJeYgqPDrQecziWbs6TDJyHLq1VnD1V1NiGw%3D",
        "image": "https://i.loli.net/2020/05/09/7F3Khj6GXYzSg4q.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "前Facebook面试官覃超带你通关算法面试，他结合自己多年面试官的经验，将高频面试题做了系统性的梳理和总结，总结出了适合大厂算法面试的LeetCode 高效切题四件套，帮你从面试中脱颖而出。课程已更新完毕，共62讲，好评如潮。",
        "link": "https://time.geekbang.org/course/intro/100019701?code=uSka4cDHATMxqMU%2FwcViKwajV-CM3oy%2FTYPTHEt8zXs%3D",
        "image": "https://i.loli.net/2020/05/09/l1BTH5m4nWwx937.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "一门为Android开发者量身定制的进阶课程，说实话，确实有点难，但如果愿意啃下去，你必然会与身边的Android开发者慢慢拉开差距。整个专栏包含3大模块：高质量应用、实现高效开发和架构演进，还有张绍文老师精心设计的练习Sample，帮助你快速掌握解决复杂问题的思路和方法。",
        "link": "https://time.geekbang.org/column/intro/100021101?code=CzZyMVt9D2DFD9KOOd%2FHWS%2FW7nYNu7p67rdgtXS2rsw%3D",
        "image": "https://i.loli.net/2020/05/09/1zFapeO6fSgEVml.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "为什么越优秀的技术公司，越强调软件工程的应用？为什么自学编程会遇到日常搬砖、增删改查的情况？扎实的“基本功”，决定了技术人的发展高度。作为软件行业知识体系的内核，无论是做技术还是管理，都绕不开，20+日常工作真实场景，及微软、谷歌大厂实践案例，帮你掌握拿来即用的软件工程方法论。",
        "link": "https://time.geekbang.org/column/intro/100023701?code=wPnxlncVDCE6XXVfHtfAAXvnNKUZqkV8JrLLozcU%2F9o%3D",
        "image": "https://i.loli.net/2020/05/09/7UBpizyPTGO9owS.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "这门课程是极客时间订阅最多的视频课，同时也是市面上性价比最高的付费教程，20000+订阅，课程由丁雪丰（市面上畅销书《SpringBoot实战》和《Spring攻略》的译者）主讲",
        "link": "https://time.geekbang.org/course/intro/100023501?code=gB%2F75zNLw1wf%2Fi9k1JXNZLQomTiX%2FrtucFOfeUXVlz4%3D",
        "image": "https://i.loli.net/2020/05/09/VgI5M72YcosrRL6.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "【完结超值优惠】《Java并发编程实战》已完结，超过1.1w人加入学习。「图文并茂+课后思考+用户留言+老师及时答复」，铸就了这个“好评超高”的专栏。真的，想要系统学并发的，推荐这个专栏。",
        "link": "https://time.geekbang.org/column/intro/100023901?code=WWJAkT6HAAZIRumT3DwmkwrN-rbHMvStnTN6lsOWksg%3D",
        "image": "https://i.loli.net/2020/05/09/5Diy3LCmvUAt9Hg.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "想要成为一名优秀的工程师，首先要搞懂计算机是怎么工作的。",
        "link": "https://time.geekbang.org/column/intro/100026001?code=EKhY-WxkjjjU6r-5XvZoTOn1zBribOeKrgbp9BN0W2o%3D",
        "image": "https://i.loli.net/2020/05/09/jVieBT6J5W4ZOMv.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "《零基础学 Java》视频课中，讲师臧萌拒绝死记硬背式的讲解，而是通过大量比喻、类比来辅助你理解抽象概念。让你边理解，边学习，掌握语法后的本质，从而不再视编程语言为“天书”。",
        "link": "https://time.geekbang.org/course/intro/100027801?code=hcWUgPZaUT23ozr-uD%2FVDGmayWP14ZDvbllTLLOLD78%3D",
        "image": "https://i.loli.net/2020/05/09/zP837RvWZ5bVjcr.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "从编程思维到架构思维的升级，这是3-5年的高级工程师将会遇到的第一个槛，早点锻炼自己的架构思维，多储备知识，才能在合适的时机升级，承担起架构设计的任务。推荐你学习这个专栏～",
        "link": "https://time.geekbang.org/column/intro/100006601?code=IV4zM5uhwnjlxtzJXppdt1cupEb6H-D9iC8s9xWPqqE%3D",
        "image": "https://i.loli.net/2020/05/09/2mHlxs1SJVMBqeR.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "像小说一样的网络协议入门课",
        "link": "https://time.geekbang.org/column/intro/100007101?code=L43XxbZJUkOnNmo-8tnojoTLEOTpki1Wlfdz8weHtyg%3D",
        "image": "https://i.loli.net/2020/05/09/Vf1ASxt8s2quNIK.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "互联网人的英语私教课",
        "link": "https://time.geekbang.org/column/intro/100051901?code=jPIIxr7KvDc15yBGdN-Hc4g3TmkDhMafbrveRzpNBww%3D",
        "image": "https://i.loli.net/2020/05/11/NEXby82VLi4ImeH.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2020-05-23 00:00"
    },
    {
        "title": "职场求生攻略，原价 ¥99，早鸟优惠+口令「zhichang8」入手仅需 ¥58",
        "link": "https://time.geekbang.org/column/intro/100052201?code=pBWk%2F-ehsvDaZHumau%2FRTBe5MJvZNMFVd8DiyzWzAtE%3D",
        "image": "https://i.loli.net/2020/05/18/BvkF7tWAqVy5fdY.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2020-05-30 00:00"
    },
    {
        "title": "微信小程序全栈开发实战，原价 ¥129，早鸟优惠+口令「52program」入手仅需 ¥89，立省 ¥40 ",
        "link": "https://time.geekbang.org/course/intro/100052401?code=gbWJRWPKzSzyCGiP60yesvVCvH%2F-FzJ4bsFuqrXppr0%3D",
        "image": "https://i.loli.net/2020/05/20/hAMp3l9Ic2qePKx.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "原价￥99，早鸟 + 口令「zhengye66」，到手价￥58",
        "link": "https://time.geekbang.org/column/intro/100052601?code=6DdY69L9bMjwjdbZpBL4kyho%2FbPd0ekjch9hM08CM8o%3D",
        "image": "https://i.loli.net/2020/05/25/JIwYclmDnCQVW27.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "原价￥129，早鸟 + 口令「bianyi666」，到手价￥89",
        "link": "https://time.geekbang.org/column/intro/100052801?code=07uHhn7RCHZkHP-CTc6mtjFgZlpZVzked%2FXMVjPHwts%3D",
        "image": "https://i.loli.net/2020/06/01/xuP5sTSdeE8UXvg.png",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "仅需 1 元，搞定 Flutter，掌握跨端开发技术，升职加薪快人一步！",
        "link": "https://t.lagou.com/4R5BRORXRk118",
        "image": "https://i.loli.net/2020/06/09/thUWMRQm6DaJZpv.png",
        "isshow": false,
        "start_time": "2020-06-09 00:00",
        "end_time": "2021-12-31 00:00"
    },
    {
        "title": "早鸟优惠 ¥55，结算用口令「weizhong8」，再减 5 元，到手 ¥50，仅限 100 人",
        "link": "https://time.geekbang.org/column/intro/100053301?code=9WTzzc7Yn8Fk8lH5ILrBfQg26wGhciLRopuzC-WEoGE%3D",
        "image": "https://i.loli.net/2020/06/09/vCkYA9M3VTsnDxl.jpg",
        "isshow": false,
        "start_time": "2020-06-10 00:00",
        "end_time": "2021-12-31 00:00"
    }
];
let showAds = adArray.filter(isShow).filter(isExpired);
let index = Math.floor(Math.random() * showAds.length);
let adItem = showAds[index];
if (adItem) {
    image.attr('src', adItem['image']);
    link.attr('href', adItem['link']);
    text.text(adItem['title']);
    var currentTime = new Date().getTime();
    if (localStorage.hideExpiredTime == null || localStorage.hideExpiredTime == undefined || localStorage.hideExpiredTime == '') {
        localStorage.hideExpiredTime = 0;
    }
    if (currentTime - localStorage.hideExpiredTime > 120000000) {
        $('.pop').show();
    }
}

$('.pop-btn-close').click(function () {
    localStorage.hideExpiredTime = currentTime;
    $('.pop').hide();
})