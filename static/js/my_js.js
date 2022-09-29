// limit text length in listview

var max = 150;
var tot, str;
$('.text').each(function () {
    str = String($(this).html());
    tot = str.length;
    str = (tot <= max)
        ? str
        : str.substring(0, (max + 1)) + "...";
    $(this).html(str);
});

// reveal search bar after scrolling 200px

$(window).scroll(function () {
    if ($(this).scrollTop() > 200) {
        $('.fixed-element').css({'display': 'block'});
    }
    else {
        $('.fixed-element').css({'display': 'none'});
    }
});
