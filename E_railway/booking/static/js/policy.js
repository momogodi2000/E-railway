$(document).ready(function() {
    // Animation for cards when hovered
    $('.card').hover(
        function() {
            $(this).addClass('shadow-lg').css('cursor', 'pointer');
        }, function() {
            $(this).removeClass('shadow-lg');
        }
    );
});
