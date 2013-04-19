function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
function show_review() {
    if(reviews) {
        var review = reviews[getRandomInt(0, reviews.length-1)]
        $('.reviews-items').html('<p>' + review + '</p>');
        setTimeout(show_review, 10000);
    }
}

$(function() {
    $('input:text').each(function(){
        $(this).prev('label').andSelf().wrapAll('<div class="control"></div>');
    });
    $('.fancybox').fancybox({});
    show_review();
});