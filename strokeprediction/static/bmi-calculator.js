var rangeSlider = function () {
    var slider = $(".row"),
        range = $(".value_range"),
        value = $(".field-text");

    slider.each(function () {
        value.each(function () {
            var value = $(this).prev().attr("value");
            $(this).html(value);
        });

        range.on("input", function () {
            $(this).next(value).html(this.value);
        });
    });
};
rangeSlider();

$("#submit").click(function () {
    var h = $("#height").val() / 100;
    var w = $("#weight").val();
    var bmi = h * h;
    bmi = w / bmi;
    bmi = bmi.toFixed(1);
    $("#bmiValue").html(bmi + " ");
    if (bmi < 18.5) {
        //Underweight
        $(".result-text").css("background", "-webkit-linear-gradient(left top, #27939D, #07658F)");
        $(".result-text").css("background", "-o-linear-gradient(bottom right, #27939D, #07658F)");
        $(".result-text").css("background", "-moz-linear-gradient(bottom right, #27939D, #07658F)");
        $(".result-text").css("background", "linear-gradient(to bottom right, #27939D, #07658F)");
        $("#bmid").html("Thiếu cân");
    } else if (18.5 <= bmi && bmi <= 24.9) {
        //Normal weight
        $(".result-text").css("background", "-webkit-linear-gradient(left top, #4FD24D, #4CA456)");
        $(".result-text").css("background", "-o-linear-gradient(bottom right, #4FD24D, #4CA456)");
        $(".result-text").css("background", "-moz-linear-gradient(bottom right, #4FD24D, #4CA456)");
        $(".result-text").css("background", "linear-gradient(to bottom right, #4FD24D, #4CA456)");
        $("#bmid").html("Bình thường");
    } else if (25 <= bmi && bmi <= 29.9) {
        //Overweight
        $(".result-text").css("background", "-webkit-linear-gradient(left top, #EF7532, #DC3A26)");
        $(".result-text").css("background", "-o-linear-gradient(bottom right, #EF7532, #DC3A26)");
        $(".result-text").css("background", "-moz-linear-gradient(bottom right, #EF7532, #DC3A26)");
        $(".result-text").css("background", "linear-gradient(to bottom right, #EF7532, #DC3A26)");
        $("#bmid").html("Thừa cân");
    } else {
        //Obese
        $(".result-text").css("background", "-webkit-linear-gradient(left top, #F73946, #FF3875)");
        $(".result-text").css("background", "-o-linear-gradient(bottom right, #F73946, #FF3875)");
        $(".result-text").css("background", "-moz-linear-gradient(bottom right, #F73946, #FF3875)");
        $(".result-text").css("background", "linear-gradient(to bottom right, #F73946, #FF3875)");
        $("#bmid").html("Béo phì");
    }
});

$('input[type="range"]').change(function () {
    var val = ($(this).val() - $(this).attr("min")) / ($(this).attr("max") - $(this).attr("min"));

    $(this).css(
        "background-image",
        "-webkit-gradient(linear, left top, right top, " +
            "color-stop(" +
            val +
            ", #F73946), " +
            "color-stop(" +
            val +
            ", #27283A)" +
            ")"
    );
});

$(".value_range").each(function () {
    var val = ($(this).val() - $(this).attr("min")) / ($(this).attr("max") - $(this).attr("min"));

    $(this).css(
        "background-image",
        "-webkit-gradient(linear, left top, right top, " +
            "color-stop(" +
            val +
            ", #F73946), " +
            "color-stop(" +
            val +
            ", #27283A)" +
            ")"
    );
});

const bmiValue = document.getElementById("bmiValue");
window.feed = function (callback) {
    var tick = {};
    tick.plot0 = parseFloat(bmiValue.innerText)
    callback(JSON.stringify(tick));
};

var myConfig = {
    type: "gauge",
    globals: {
        fontSize: 25,
    },
    plotarea: {
        marginTop: 80,
    },
    plot: {
        size: "100%",
        valueBox: {
            placement: "center",
            text: "%v", //default
            fontSize: 35,
            rules: [
                {
                    rule: "%v >= 30",
                    text: "%v<br>Béo phì",
                },
                {
                    rule: "%v < 30 && %v > 25",
                    text: "%v<br>Thừa cân",
                },
                {
                    rule: "%v < 25 && %v > 18",
                    text: "%v<br>Lý tưởng",
                },
                {
                    rule: "%v <  18",
                    text: "%v<br>Thiếu cân",
                },
            ],
        },
    },
    tooltip: {
        borderRadius: 5,
    },
    scaleR: {
        aperture: 180,
        minValue: 0,
        maxValue: 83,
        step: 20,
        center: {
            visible: false,
        },
        tick: {
            visible: false,
        },
        item: {
            offsetR: 0,
            rules: [
                {
                    rule: "%i == 9",
                    offsetX: 15,
                },
            ],
        },
        labels: ["0", "18", "25", "30"],
        ring: {
            size: 50,
            rules: [
                {
                    rule: "%v <= 18",
                    backgroundColor: "#E53935",
                },
                {
                    rule: "%v > 18 && %v < 25",
                    backgroundColor: "#EF5350",
                },
                {
                    rule: "%v >= 25 && %v < 30",
                    backgroundColor: "#FFA726",
                },
                {
                    rule: "%v >= 30",
                    backgroundColor: "#29B6F6",
                },
            ],
        },
    },
    refresh: {
        type: "feed",
        transport: "js",
        url: "feed()",
        interval: 1500,
        resetTimeout: 1000,
    },
    series: [
        {
            values: [0], // starting value
            backgroundColor: "black",
            indicator: [10, 10, 10, 10, 0.75],
            animation: {
                effect: 2,
                method: 1,
                sequence: 4,
                speed: 1000,
            },
        },
    ],
};

zingchart.render({
    id: "myChart",
    data: myConfig,
    height: "400",
    width: "100%",
});
