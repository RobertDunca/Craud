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

