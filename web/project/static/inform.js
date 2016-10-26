window.onload = function() {
	var score =document.getElementById("get-score");
	var scoreNum = document.getElementById("score-num");
	var flag = 0;
    $(".help").fadeOut(0);
    $(".sos").fadeOut(0);
    $("#map").fadeOut(0);
	
    score.onclick = function() {
		if (flag == 0) {
			var pre = parseInt(scoreNum.innerHTML);
			scoreNum.innerHTML = ++pre;
			score.innerHTML = "已签到";
			score.id="get-score1";
			flag++;
		}
	};
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
function lineChart() {
	var ctx = document.getElementById('line').getContext("2d");
        var data = {
            labels: ["2015-01", "2015-02", "2015-03", "2015-04", "2015-05", "2015-06","2015-07","2015-08","2015-09"],
            datasets: [{
                label: "",
                fillColor: "rgba(256,256,256,0)",
                strokeColor: "#2A77E3",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#2A77E3",
                pointHighlightFill: "#2A77E3",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [6, 7, 3, 5, 4, 9, 10, 1, 2]
            },
            {
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "#037B4A",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#037B4A",
                pointHighlightFill: "#037B4A",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [2, 9, 6, 3, 5, 4, 1, 5, 8]
            },
            {
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "rgb(153,0,0)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "rgb(153,0,0)",
                pointHighlightFill: "rgb(153,0,0)",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [5, 2, 8, 4, 3, 4, 1, 7, 6]
            }
            ]
        };
        var TotalChart = new Chart(ctx).Line(data, {
            bezierCurveTension: 0,
            bezierCurve: false,
            tooltipTemplate: "<%= value %>个",
            scaleOverride: true,
            scaleSteps: 9.5,
            scaleStepWidth: 1,
            scaleStartValue: 1
        });
}

function lineChartQuestion() {
        var ctx = document.getElementById('line').getContext("2d");
        var data = {
            labels: ["2015-01", "2015-02", "2015-03", "2015-04", "2015-05", "2015-06","2015-07","2015-08","2015-09"],
            datasets: [{
                label: "",
                fillColor: "rgba(256,256,256,0)",
                strokeColor: "#2A77E3",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#2A77E3",
                pointHighlightFill: "#2A77E3",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [6, 7, 3, 5, 4, 9, 10, 1, 2]
            }]
        };

        var questionChart = new Chart(ctx).Line(data, {
            bezierCurveTension: 0,
            bezierCurve: false,
            tooltipTemplate: "<%if (label){%><%=label%> 数量：<%}%><%= value %>个",
            scaleOverride: true,
            scaleSteps: 9.5,
            scaleStepWidth: 1,
            scaleStartValue: 1
        });
}
function lineChartHelp() {
        var ctx = document.getElementById('line').getContext("2d");
        var data = {
            labels: ["2015-01", "2015-02", "2015-03", "2015-04", "2015-05", "2015-06","2015-07","2015-08","2015-09"],
            datasets: [{
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "#037B4A",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#037B4A",
                pointHighlightFill: "#037B4A",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [2, 9, 6, 3, 5, 4, 1, 5, 8]
            }]
        };

        var helpChart = new Chart(ctx).Line(data, {
            bezierCurveTension: 0,
            bezierCurve: false,
            tooltipTemplate: "<%if (label){%><%=label%> 数量：<%}%><%= value %>个",
            scaleOverride: true,
            scaleSteps: 9.5,
            scaleStepWidth: 1,
            scaleStartValue: 1
        });
}
function lineChartSOS() {
        var ctx = document.getElementById('line').getContext("2d");
        var data = {
            labels: ["2015-01", "2015-02", "2015-03", "2015-04", "2015-05", "2015-06","2015-07","2015-08","2015-09"],
            datasets: [{
                label: "",
                fillColor: "rgba(220,220,220,0)",
                strokeColor: "rgb(153,0,0)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "rgb(153,0,0)",
                pointHighlightFill: "rgb(153,0,0)",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [5, 2, 8, 4, 3, 4, 1, 7, 6]
            }]
        };

        var SOSChart = new Chart(ctx).Line(data, {
            bezierCurveTension: 0,
            bezierCurve: false,
            tooltipTemplate: "<%if (label){%><%=label%> 数量：<%}%><%= value %>个",
            scaleOverride: true,
            scaleSteps: 9.5,
            scaleStepWidth: 1,
            scaleStartValue: 1
        });
}

function changeTitle(str) {
    var ele = document.getElementById("#h1");
    ele.style.fontSize = '22px';
    if (str=="question") {
        ele.innerHTML = "您已累计回答了123次，提问了456次";
    }
    else if (str == "help") {
        ele.innerHTML = "您已累计帮助了456次，施助了789次";
    }
    else if (str == "SOS") {
        ele.innerHTML = "您已累计求救了003次，施救了45次";
    }
}

// 启动
setTimeout(function() {
   lineChart()
}, 0)



//  悬赏爱心币的函数
/*
function coin(str) {
    var ele = document.getElementById('coinnum');
    if (str == 'add') {

        console.log(ele.innerHTML)
        ele.innerHTML = parseInt(ele.innerHTML) + 1;
        console.log("ele.innerHTML" + ele.innerHTML)
        console.log("ele.value" + ele.value)
    }
    else if (str == 'des') {
        if (ele.innerHTML <= 0)
            ele.innerHTML = 0;
        else
            ele.innerHTML = parseInt(ele.innerHTML) - 1;
    }
}
*/

function coin(str) {
    var ele = document.getElementById('coinnum');
    if (str == 'add')
        ele.value = parseInt(ele.value) + 1;
    else if (str == 'des') {
        if (ele.value <= 0)
            ele.value = 0;
        else
            ele.value = parseInt(ele.value) - 1;
    }
}









