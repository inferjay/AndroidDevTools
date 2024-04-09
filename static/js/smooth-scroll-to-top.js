if (location.href.indexOf('?id=') > 0) {
    let url = new URL(location.href);
    let id = url.searchParams.get('id');
    const dom = document.getElementById(`${id}`);
    window.scrollTo({
        top: dom.offsetTop,
        behavior: "smooth"
    })
}

$(function () {
    // Syntax highlight code blocks.
    //prettyPrint();

    // Spy on scroll position for real-time updating of current section.
    $('body').scrollspy();

    // Use smooth-scroll for internal links.
    $('a').smoothScroll();

    // Enable tooltips on the header nav image items.
    $('.menu').tooltip({
        placement: 'bottom',
        trigger: 'hover',
        container: 'body',
        delay: {
            show: 500,
            hide: 0
        }
    });
});