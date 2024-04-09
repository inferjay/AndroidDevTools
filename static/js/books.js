var isShowBookList = false;
var books = {
  title: "书",
  showCount: 15,
  data: [
    {
      title: "无界面交互:潜移默化的UX设计方略",
      url: "http://t.cn/Rotrq7Z",
      description:
        "本书通过丰富的示例和生动的讲解，深刻揭示了当今屏幕至上的界面设计的种种怪象。本书呼吁将设计的重心由界面转向对用户个性化需求的关怀，并提出了无界面交互设计方略的三个原则以构建优质用户体验：贴合日常生活流程，做电脑的主人而非仆人，适应个体情况。",
      img_url:
        "http://wx3.sinaimg.cn/large/006tNc79ly1fgt2uu0odfj304605gdfw.jpg",
      tags: "Design,UX",
      isshow: false,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "极简主义:风靡欧美的工作与生活理念",
      url: "http://t.cn/RotrQOG",
      description:
        "本书适合所有想提高做事效率、提升人生幸福感的人士阅读。如果你真的想简化繁重的工作事务和日常生活，请一定要记住：好方法往往最简单。",
      img_url: "https://i.loli.net/2020/02/09/u9vEwL1exS4ghHK.jpg",
      tags: "工作,生活",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "Gradle for Android中文版",
      url: "http://t.cn/RotVOIb",
      description:
        "本书共分9章，依次介绍了Gradle的基础知识、基本自定义构建、依赖管理、创建构建Variants、管理多模块构建、运行测试、创建tasks和插件、设置持续集       成，以及高级自定义构建。",
      img_url: "https://p.ipic.vip/35g9fz.jpg",
      tags: "Android,Gradle",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "增长黑客实战",
      url: "http://t.cn/RotfVPF",
      description:
        "本书围绕硅谷前沿的增长黑客职业，讲解增长理念的树立、增长团队的组建、流程制度的创立、技术营销的运用等团队运营成功实战经验。本书适合希望成功创业       的CEO、公司经理、开发人员、产品经理和市场运营人员，以及任何有创意并且想创业的人。",
      img_url: "https://p.ipic.vip/m2afmt.jpg",
      tags: "运营,Growth Hacking",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "提问的智慧",
      url: "https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md",
      description: "本指南将教你如何正确的提问以获得你满意的答案。",
      img_url: "https://p.ipic.vip/yw570k.jpg",
      tags: "OpenSource Book,提问",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "A Primer on Bézier Curves",
      url: "https://pomax.github.io/bezierinfo/zh-CN/",
      description: "一本讲解贝塞尔曲线的开源书",
      img_url: "https://p.ipic.vip/yw570k.jpg",
      tags: "OpenSource Book,贝塞尔曲线",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "免费的编程中文书籍索引",
      url: "http://siberiawolf.com/free_programming/index.html",
      description:
        "本索引包含：国外程序员在 stackoverflow 推荐的程序员必读书籍，中文版；stackoverflow 上的程序员应该阅读的非编程类书籍有哪些？      中文版；github 上的一个流行的编程书籍索引 中文版",
      img_url: "https://i.loli.net/2020/02/09/dtWTrUp968HaiBk.jpg",
      tags: "OpenSource Book,Free",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "人类简史：从动物到上帝",
      url: "http://t.cn/Rot8C7R",
      description:
        "以色列新锐历史学家的一部重磅作品。从十万年前有生命迹象开始到21世纪资本、科技交织的人类发展史。十万年前，地球上至少有六个人种，为何今天却只剩下      了我们自己？我们曾经只是非洲角落一个毫不起眼的族群，对地球上生态的影响力和萤火虫、猩猩或者水母相差无几。为何我们能登上生物链的顶端，最终成为地球的主宰？",
      img_url: "https://i.loli.net/2020/02/09/st6ADOUTgEpmY4i.jpg",
      tags: "社会学",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "重来:更为简单有效的商业思维",
      url: "http://t.cn/RotRYYU",
      description:
        "大多数的企业管理的书籍都会告诉你：制定商业计划、分析竞争形势、寻找投资人等等。如果你要找的是那样的书，那么把《重来:更为简单有效的商业思维》放       回书架吧。《重来:更为简单有效的商业思维》呈现的是一种更好、更简单的经商成功之道。",
      img_url: "https://p.ipic.vip/6d8mry.jpg",
      tags: "创业,商业",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "重新定义团队:谷歌如何工作",
      url: "http://t.cn/RotEwoG",
      description:
        "在谷歌，人始终被当作企业最重要的财富，谷歌管理层始终将发掘、培养和留住人才，作为企业高战略，这是谷歌成为幸福企业和成功企业的根本。正如作者所说       ，谷歌的这些原则对任何团队的组建和管理都适用。不管你是苦于找不到合伙人的初创公司老板，还是面临好人才跳槽的企业经理人，抑或是面对互联网转型的企业高管，都能从书     中重新发现人才的重要性和团队的价值。",
      img_url: "https://p.ipic.vip/6rkyxv.jpg",
      tags: "谷歌,创业,运营,招聘",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "鱼羊野史(第1卷)",
      url: "http://t.cn/RotEnk4",
      description:
        "历史，有的时候是故事，有的时候是事故，有的时候山重水复疑无路。 人类，有的时候聪明，有的时候傻，但始终在进化。       历史不是镜子，历史是开了又落的花，朝花夕拾, 跟高晓松一起，重温故国、故城、故人芳华刹那",
      img_url: "https://p.ipic.vip/5vlyx2.jpg",
      tags: "历史",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "重新定义公司:谷歌是如何运营的",
      url: "http://t.cn/RotnCxs",
      description:
        "今日的谷歌是全球最具标志性的企业，在各个领域都有创新突破，并向技术的极限推进。《重新定义公司：谷歌是如何运营的》作者是谷歌执行董事长埃里克·施       密特和前高级副总裁乔纳森·罗森伯格，他们亲自分享十余年来帮助谷歌成长所领悟到的管理启示：科技正在改变商业的方方面面，这种改变速度空前，而且仍在加速，公司若想在     互联网时代站稳脚跟，就要制定新的商业规则。",
      img_url: "https://p.ipic.vip/0ejz2f.jpg",
      tags: "谷歌,创业,运营",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "腾讯传1998—2016",
      url: "http://t.cn/RotuPIN",
      description:
        "从1998年开始创业到成为世界级互联网巨头，腾讯以即时通信工具起步，逐渐进入社交网络、互动娱乐、网络媒体、电子商务等领域，在超高速发展的同时亦饱      受争议，在“3Q大战”的激烈冲突之后又进一步走向开放……腾讯的发展路径，亦是中国互联网企业成长的缩影。我们可以看到，中国的互联网人在应用性迭代和对本国消费者的行为   了解上，找到了自己的办法，并开始领跑全球。",
      img_url: "https://p.ipic.vip/e5s6z2.jpg",
      tags: "腾讯,传记",
      isshow: false,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "把时间当作朋友(第3版)",
      url: "http://t.cn/RotuIRJ",
      description:
        "从心智成长的角度来谈自我积累。李笑来老师通过自己职业生涯中遇到的事例，告诉我们：如何打开心智，如何运用心智来和时间做朋友，从而开启人生的成功旅       程。畅销多年，虽经反复咀嚼依然不断有新的启发，令人受用至今——这就是本书的魅力！",
      img_url:
        "http://wx2.sinaimg.cn/large/006tNc79ly1fgt2uu8drjj304605g74f.jpg",
      tags: "认知,心智,时间",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "从0到1:开启商业与未来的秘密",
      url: "http://t.cn/RotuRhL",
      description:
        "硅谷创投教父、PayPal创始人作品，斯坦福大学改变未来的一堂课，为世界创造价值的商业哲学。在科技剧烈改变世界的今天，想要成功，你必须在一切发生之     前研究结局。你必须找到创新的独特方式，让未来不仅仅与众不同，而且更加美好。从0到1，为自己创造无限的机会与价值！",
      img_url: "https://p.ipic.vip/wdc4jx.jpg",
      tags: "创业",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "把你的英语用起来!(新版) ",
      url: "http://t.cn/Rot3UrV",
      description:
        "在这本书中，作者刘晓光和伍君仪以自己英语逆袭的亲身经历入手，提供了一套理论清晰、操作性强的英语训练体系，向所有英语学习者传达了这样的理念：语言学习没有捷径，但没有捷径并不意味着学习者要坚持下去一定会十分艰辛。",
      img_url: "https://p.ipic.vip/ojg2q2.jpg",
      tags: "英语",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "1368个单词就够了",
      url: "http://t.cn/Rot3YSK",
      description:
        "这本书是作者王乐平先生历时4年研发，在教学过程中更好的实现了本书思想的实际指导作用。这本书的基础在于：中国人背了多年的单词，学语法，练习听力和       口语，参加了多种类型的考试，但由于缺乏语言环境，很多人在真正使用英语的时候，还是出现表达障碍。",
      img_url: "https://p.ipic.vip/w1o6zw.jpg",
      tags: "英语",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "每天最重要的2小時",
      url: "http://t.cn/Rot1JHR",
      description:
        "本書作者戴維斯告訴我們，企圖以效法電腦效率的方式來管理我們的時間，注定要失敗。他以淺顯易懂且有趣的文筆生動地解釋行為科學，告訴我們一天當中真正       有效率的關鍵時刻，而且一樣重要的是，他也告訴我們如何用更好的方式，安排其他效率沒那麼好的平凡時刻。",
      img_url:
        "http://wx1.sinaimg.cn/large/006tNc79ly1fgt2utawcdj304605gaa7.jpg",
      tags: "时间",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "增长黑客:创业公司的用户与收入增长秘籍",
      url: "http://t.cn/RotBEcK",
      description:
        "增长黑客”这一概念近年来兴起于美国互联网创业圈，最早是由互联网创业者Sean        Ellis提出。增长黑客是介于技术和市场之间的新型团队角色，主要依靠技术和数据的力量来达成各种营销目标，而非传统意义上靠砸钱来获取用户的市场推广角色。",
      img_url:
        "http://wx2.sinaimg.cn/large/006tNc79ly1fgt2uut31hj304605gwf3.jpg",
      tags: "创业,Growth Hacking",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "第一行代码——Android（第2版）",
      url: "http://t.cn/Roluf0E",
      description:
        "本书基于Android 7.0对第1版进行了全面更新，将所有知识点都在最新的Android系统上进行了重新适配，使用全新的Android Studio开发工具代替之前的Eclipse，并添加了对Material Design、运行时权限、多窗口模式、Gradle、RecyclerView、百分比布局、OkHttp、Lambda表达式等全新知识点的详细讲解。",
      img_url:
        "http://wx4.sinaimg.cn/large/006tKfTcly1fh120qi0t9j304605gaak.jpg",
      tags: "Android,Material Design,RecyclerView,Gradle, Android Studio,OkHttp,Lambda",
      isshow: false,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "Android 应用安全防护和逆向分析",
      url: "https://amazon.cn/gp/product/B0788XV9WC/ref=as_li_tl?ie=UTF8&camp=536&creative=3200&creativeASIN=B0788XV9WC&linkCode=as2&tag=androiddevtools-bottom-book-",
      description:
        "本书全面介绍Android应用的安全防护方法与逆向分析技术，分为四篇：基础篇、防护篇、工具篇、操作篇，共26章。基础篇包括第1~7章，主要介绍移动应用安全的基础知识，包括Android中NDK开发知识、逆向中需要用到的命令、编译之后的apk包含的四类主要文件格式解析等。防护篇包括第8~14章，主要介绍移动应用安全防护的相关技术，包括混淆、签名校验、反调试检测等安全策略，Android应用升级权限、降低权限等，配置文件中的问题，应用签名机制，apk的加固策略，so文件的加固策略等。工具篇包括第15~19章，主要介绍逆向分析常用的工具以及使用场景，包括如何开启设备的总调试开关，反编译利器apktool、Jadx、Xposed、CydiaSubstrate等。操作篇包括第20~26章，主要介绍Android中的逆向分析技巧，包括静态方式和动态方式，介",
      img_url:
        "https://wx2.sinaimg.cn/large/006tNc79ly1fmojaxsu2kj304605gq30.jpg",
      tags: "Android,安全,逆向",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "Android Things 中文文档社区预览版",
      url: "https://atdocs.cn/",
      description:
        "全球已经有很多开发者使用 Android Things 开发出了非常有意思的应用，使用 Android Things 技术在物联网领域占得一席之地。这一次，我们希望中国的开发者也能参与，不掉队。我们与官方取得联系，在 Android Things 的文档最近进行的一次大改动之后，计划招募志愿者将文档中文化，并持续跟进。欢迎大家不停的 Review 这份翻译文档。在我们的社区校对完成之后，文档就是 Google Developers 中文官方文档。",
      img_url:
        "https://wx2.sinaimg.cn/large/006tKfTcly1fmpjxtm14yj304605gwer.jpg",
      tags: "Android,Android Things,物联网,IoT",
      isshow: false,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
    {
      title: "JavaScript Promise 迷你书（中文版）",
      url: "http://liubin.org/promises-book/",
      description:
        "本书的目的是以目前还在制定中的 ECMAScript 6 Promises 规范为中心，着重向各位读者介绍 JavaScript 中对 Promise 相关技术的支持情况。通过阅读本书，我们希望各位读者能在下面三个目标上有所收获：1.学习 Promise 相关内容，能熟练使用 Promise 模式并进行测试；2.学习 Promise 适合什么、不适合什么，知道 Promise 不是万能的，不能什么都想用 Promise 来解决；3.以 ES6 Promises 为基础进行学习，逐渐发展形成自己的风格。像上面所提到的那样，本书主要是以 ES6 Promises，即 JavaScript 的标准规范为基础的、Promise 的相关知识为主要讲解内容。",
      img_url:
        "https://wx3.sinaimg.cn/large/006tKfTcly1fmpktm97s8j304605g3ys.jpg",
      tags: "JavaScript,Promise,ECMAScript 6",
      isshow: true,
      isShowCover: true,
      isad: false,
      ad_config: {
        category: "AD",
        action: "click",
        label: "",
        value: "",
        nodeid: "",
      },
      style: {
        isRound: true,
      },
    },
  ],
};

Array.prototype.randomDiffElement = function (last) {
  if (this.length == 0) {
    return;
  } else if (this.length == 1) {
    return this[0];
  } else {
    var num = 0;
    do {
      num = Math.floor(Math.random() * this.length);
    } while (
      Array.isArray(last) ? last.includes(this[num]) : this[num] == last
    );
    return this[num];
  }
};

function isEquals() {}

var buildBookItem = function (book) {
  var link =
    '<a href="' + book.url + '" target="_blank" title="' + book.description;
  link =
    link +
    (book.isad
      ? '" onclick="trackOutboundLink(\'' +
        book.url +
        "', '" +
        book.ad_config.category +
        "-" +
        book.ad_config.label +
        "', '" +
        book.ad_config.action +
        "');\" >"
      : '" >');
  if (book.isShowCover && book.img_url) {
    var imgClass;
    if (book.style.isRound) {
      imgClass = "carousel-inner img-responsive img-rounded";
    } else {
      imgClass = "carousel-inner img-responsive";
    }
    link = link + '<img class="' + imgClass + '" src="' + book.img_url + '">';
  }
  return "<li>" + link + "</a></li>";
};

var initBookList = function () {
  if (isShowBookList && books) {
    if (books.title && books.title.length > 0) {
      $("#books-list").find("#book-list-title").text(books.title);
    } else {
      $("#books-list").find("#book-list-title").hide();
    }
    if (books.data && books.data.length > 0) {
      var bookListBox = $("#books-list ul");
      var lastRandomBook = [];
      for (var i = 0; i < books.showCount; i++) {
        var book = books.data.filter(isShow).randomDiffElement(lastRandomBook);
        if (book) {
          bookListBox.append(buildBookItem(book));
        }
        lastRandomBook.push(book);
      }
      if ($(bookListBox).children()) {
        $("#books-list").show();
      }
    }
  }
};

function addBannerItemClickEvent() {
  var bannerItems = $("#ad-banner-list").find("ul>li").toArray();
  console.log(Array.isArray(bannerItems));
  bannerItems.forEach(function (element) {
    var link = $(element).attr("data-link"),
      tag = $(element).attr("data-tag"),
      type = $(element).attr("data-event-type");
    $(element)
      .unbind("click")
      .bind("click", function (event) {
        trackOutboundLink(link, tag, type);
        window.location.href = link;
        event.preventDefault();
        event.stopPropagation();
        console.log(link);
      });
  });
}
initBookList();
addBannerItemClickEvent();
