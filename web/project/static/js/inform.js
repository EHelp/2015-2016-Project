window.onload = function() {
	var score =document.getElementById("get-score");
	var scoreNum = document.getElementById("score-num");
	var flag = 0;
    var info_data;
    $(".help").fadeOut(0);
    $(".sos").fadeOut(0);
    $("#map").fadeOut(0);
	
 //    score.onclick = function() {
	// 	if (flag == 0) {
	// 		var pre = parseInt(scoreNum.innerHTML);
	// 		scoreNum.innerHTML = ++pre;
	// 		score.innerHTML = "已签到";
	// 		score.id="get-score1";
	// 		flag++;
	// 	}
	// };

    
    var xsrf_t = getCookie("_xsrf");
    $.post("/account/record", {"userId": $("#user-id").val(), "_xsrf": xsrf_t},
        function(data, status) {
            info_data = eval('(' + data + ')');
            lineChart(info_data);

            $("span.question_t").click(function() {
                lineChartQuestion(info_data);
                changeTitle("question", info_data);
            });

            $("span.help_t").click(function() {
                lineChartHelp(info_data);
                changeTitle("help", info_data);
            });

            $("span.sos_t").click(function() {
                lineChartSOS(info_data);
                changeTitle("SOS", info_data);
            });

            $("#chart-state").click(function() {
                lineChart(info_data);
                changeTitle("myFootprint", info_data);
            });
        }
    );
}

function getCookie(name) {
    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return c ? c[1] : undefined;
}

$(function() {
	//start a map
	var map = new AMap.Map('map');
	//end a map


	//right key for contact
	$(".contact-tabs").each(function() {
		$(this).contextMenu("contact-tabs-list", 
		{
		});
	});
	$(".person-li").each(function() {
		$(this).contextMenu("contact-tabs-persons", 
		{
		});
	});

    $("#help").click(function() {
        $(".question").fadeOut(500);
        $(".help").fadeIn(500);
        $(".sos").fadeOut(500);
        $("#map").fadeIn(500);
    });

    $("#sos").click(function() {
        $(".question").fadeOut(500);
        $(".help").fadeOut(500);
        $(".sos").fadeIn(500);
        $("#map").fadeIn(500);
    });

    $("#question").click(function() {
        $(".question").fadeIn(500);
        $(".help").fadeOut(500);
        $(".sos").fadeOut(500);
        $("#map").fadeOut(500);
    });
});
// chart.js
//  Chart.js代码

function lineChart(data) {
    var ctx = document.getElementById('line').getContext("2d");
        var data = {
            labels: ["最近一个月", "过去第1个月", "过去第2个月", "过去第3个月", "过去第4个月", "过去第5个月"],
            datasets: [{
                label: "",
                fillColor: "rgba(256,256,256,0)",
                strokeColor: "#2A77E3",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#2A77E3",
                pointHighlightFill: "#2A77E3",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["question"]["ask_date"]
            },
            {
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "#037B4A",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#037B4A",
                pointHighlightFill: "#037B4A",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["help"]["ask_date"]
            },
            {
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "rgb(153,0,0)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "rgb(153,0,0)",
                pointHighlightFill: "rgb(153,0,0)",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["save"]["ask_date"]
            },
            {
                label: "",
                fillColor: "rgba(256,256,256,0)",
                strokeColor: "#4B0082",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#4B0082",
                pointHighlightFill: "#4B0082",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["question"]["reply_date"]
            },
            {
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "#D2691E",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#D2691E",
                pointHighlightFill: "#D2691E",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["help"]["reply_date"]
            },
            {
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "#00008B",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#00008B",
                pointHighlightFill: "#00008B",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["save"]["reply_date"]
            }]
        };
        var TotalChart = new Chart(ctx).Line(data, {
            bezierCurveTension: 0,
            bezierCurve: false,
            tooltipTemplate: "<%= value %>个",
            scaleOverride: true,
            scaleSteps: 35.0,
            scaleStepWidth: 1,
            scaleStartValue: 0
        });

}

function lineChartQuestion(data) {
        var ctx = document.getElementById('line').getContext("2d");
        var data = {
            labels: ["过去第5个月", "过去第4个月", "过去第3个月", "过去第2个月", "过去第1个月", "最近一个月"],
            datasets: [{
                label: "",
                fillColor: "rgba(256,256,256,0)",
                strokeColor: "#2A77E3",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#2A77E3",
                pointHighlightFill: "#2A77E3",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["question"]["ask_date"]
            },
            {
                label: "",
                fillColor: "rgba(256,256,256,0)",
                strokeColor: "#4B0082",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#4B0082",
                pointHighlightFill: "#4B0082",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["question"]["reply_date"]
            }]
        };

        var questionChart = new Chart(ctx).Line(data, {
            bezierCurveTension: 0,
            bezierCurve: false,
            tooltipTemplate: "<%if (label){%><%=label%> 数量：<%}%><%= value %>个",
            scaleOverride: true,
            scaleSteps: 35.0,
            scaleStepWidth: 1,
            scaleStartValue: 0
        });
}
function lineChartHelp(data) {
        var ctx = document.getElementById('line').getContext("2d");
        var data = {
            labels: ["过去第5个月", "过去第4个月", "过去第3个月", "过去第2个月", "过去第1个月", "最近一个月"],
            datasets: [{
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "#037B4A",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#037B4A",
                pointHighlightFill: "#037B4A",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["help"]["ask_date"]
            },
            {
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "#D2691E",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#D2691E",
                pointHighlightFill: "#D2691E",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["help"]["reply_date"]
            }]
        };

        var helpChart = new Chart(ctx).Line(data, {
            bezierCurveTension: 0,
            bezierCurve: false,
            tooltipTemplate: "<%if (label){%><%=label%> 数量：<%}%><%= value %>个",
            scaleOverride: true,
            scaleSteps: 35.0,
            scaleStepWidth: 1,
            scaleStartValue: 0
        });
}
function lineChartSOS(data) {
        var ctx = document.getElementById('line').getContext("2d");
        var data = {
            labels: ["过去第5个月", "过去第4个月", "过去第3个月", "过去第2个月", "过去第1个月", "最近一个月"],
            datasets: [{
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "rgb(153,0,0)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "rgb(153,0,0)",
                pointHighlightFill: "rgb(153,0,0)",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["save"]["ask_date"]
            },
            {
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "#00008B",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#00008B",
                pointHighlightFill: "#00008B",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data["currentUserRecordInfo"]["save"]["reply_date"]
            }]
        };

        var SOSChart = new Chart(ctx).Line(data, {
            bezierCurveTension: 0,
            bezierCurve: false,
            tooltipTemplate: "<%if (label){%><%=label%> 数量：<%}%><%= value %>个",
            scaleOverride: true,
            scaleSteps: 35.0,
            scaleStepWidth: 1,
            scaleStartValue: 0
        });
}

function changeTitle(str, data) {
    var ele = document.getElementById("#header1");
    var innerHTML = "";
    var sample = document.getElementsByName("sampleColor");
    ele.style.fontSize = '22px';
    $("#header1").css("font-size", "22px");
    if (str == "myFootprint") ele.style.fontSize = '36px';;

    if (str=="question") {
        innerHTML = "您已累计回答了" + data["currentUserRecordInfo"]["question"]["reply_num"] + "次，提问了" + data["currentUserRecordInfo"]["question"]["ask_num"] + "次";
        for (var i = 0; i < 4; i++) {
            if (i == 1)
                sample[i].style.display = 'block';
            else
                sample[i].style.display = 'none';
        }
    }
    else if (str == "help") {
        innerHTML = "您已累计施助了" + data["currentUserRecordInfo"]["help"]["reply_num"] + "次，求助了" + data["currentUserRecordInfo"]["help"]["ask_num"] + "次";
        for (var i = 0; i < 4; i++) {
            if (i == 2)
                sample[i].style.display = 'block';
            else
                sample[i].style.display = 'none';
        }
    }
    else if (str == "SOS") {
        innerHTML = "您已累计施救了" + data["currentUserRecordInfo"]["save"]["reply_num"] + "次，求救了" + data["currentUserRecordInfo"]["save"]["ask_num"] + "次";
        for (var i = 0; i < 4; i++) {
            if (i == 3)
                sample[i].style.display = 'block';
            else
                sample[i].style.display = 'none';
        }
    } else if (str == "myFootprint") {
        innerHTML = "2015年易助个人数据统计";
        for (var i = 0; i < 4; i++) {
            if (i == 0)
                sample[i].style.display = 'block';
            else
                sample[i].style.display = 'none';
        }
    }
    ele.innerHTML = innerHTML;

   //   $("h1#h1").html("innerHTML");
}
