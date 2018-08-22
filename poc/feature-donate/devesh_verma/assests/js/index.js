$(document).ready(function() {
    "use strict";

    $(".count").each(function() {

        var $this = $(this),
            $container = $this.closest(".container__counter"), // set this to element other than the actual element that is updating the number as counter increments
            $value = $this.data("number");

        $container.velocity(
            { tween: [$value, 0] },
            {
                easing: "easeOutCirc",
                delay: 500,
                duration: 9000, // this determines the number of "progres" steps
                progress: function(elements, complete, remaining, start, tweenValue) {
                    return $this.text(Math.round(tweenValue).toLocaleString());
                }
            }
        );
    });
});
