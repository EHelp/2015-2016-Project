$(document).ready(function() {

  	var ws = new WebSocket("ws://120.24.208.130:8000/socket/question");
  	// var ws = new WebSocket("ws://localhost:8000/socket/question");

	ws.onopen = function (event) {};

	ws.onmessage = function(event) {

	    var data = $.parseJSON(event.data);
	    if (data["resp_status"] == 200) {
		    if (data["mesType"] == 0) {
		    	add_questions(data);
		    } else {
		    	add_comment(data);
		    }
		} else {
			//to indicate the failure.
			alert("发表提问失败！");
			//您的爱心币不足
			var id = $("#user-id").val();
			//window.location.href = "/" + id;
			$("#lovecoinnum").val("0");
		}
	};
	
	$("#comment_submit").click(function(check) {
		check.preventDefault();


		var title = $("#title").val();
        var content = $("#content").val();

        // "love_coin": $("#lovcoinnum").val(), "content": 
        var reg = new RegExp("^ +$");
        if (title == "" || content == "" || title.match(reg) || content.match(reg)) {

          alert("输入不能为空");
          return;
        }

        // alert($("#lovlovcoinnum").val());
		var username = $("#user-name").val();
		var userobj = {"mesType": 0, "id": $("#user-id").val(), "userName": username, "title": $("#title").val(), "love_coin": $("#lovecoinnum").val(), "content": $("#content").val()};
        //alert(JSON.stringify(userobj));
        ws.send(JSON.stringify(userobj));
   		//add_questions();
        $("#content").val("");
        $("#title").val("");
        $("#lovecoinnum").val("0");
	});

	$("button.answer").click(function(check) {
		check.preventDefault();
		var info = $(this).parent().parent().parent().parent().children();
		var eventId = parseInt($(info[0]).val());
		var userId = parseInt($(info[2]).val());
		var authorId = parseInt($(info[1]).val());
		var username = $("#user-name").val();
		/*var eventId = panelParent.children("input.eventId").val();
		var userId = panelParent.children("input.userId").val();
		var authorId = panelParent.children("input.authorId").val();
		var mesInput = $(this).parentsUntil("div.input-group");*/
		var mesInput = $(this).parent().parent().children();
		var content = $(mesInput[0]).val();
		var userobj = {"mesType": 1, "id": userId, "userName": username, "event_id": eventId, "author_id": authorId, "content": content};

        ws.send(JSON.stringify(userobj));
		$(mesInput[0]).val("");
	});


	/*
	$("#modify_user").click(function(event) {
		event.preventDefault();
		id = $("#user-id").val();
		window.location.href = "/account/userinfo/modify/" + id;

	});

	$("#index").click(function(event) {

		event.preventDefault();
		id = $("#user-id").val();
		window.location.href = "/" + id;
	});
	*/
	

} );

function add_comment(data) {
	$("div.piece").each(function() {
		var eventid = $(this).children("input.event_id").val();
		if (eventid == data["event_id"]) {
			var parent = $(this).children("div.comment").children("div.old-comment");

			/*alert(data["launcher_profile"]);*/
			var new_img4 = $("<img></img>").attr("src", "static/images/head/" + data["launcher_profile"]);
			var new_a2 = $("<a></a>").attr("href", "").append(new_img4);

			
			DateTime = new Date(data["date"]);
			data["date"] = DateTime.toLocaleString();
			//alert(data["date"]);
			var new_p5 = $("<p></p>").text(data["userName"] + ":");
			var new_p6 = $("<p></p>").text(data["date"]);
			var new_div3 = $("<div></div>").addClass("comment-time").append(new_p5, new_p6);

			var new_p7 = $("<p></p>").text(data["content"]);
			var new_div4 = $("<div></div>").addClass("comment-text").append(new_p7);

			var new_div5 = $("<div></div>").addClass("comment-piece").append(new_a2, new_div3, new_div4);
			$(parent).append(new_div5);
			/*
			if (.length == 0) {
				var btnTemp = $(this).children("div").children("div.input-group");
				$(new_comment).insertBefore(btnTemp);
			} else {
				$(new_comment).insertAfter(p_t[p_t.length-1]);
			}*/

 			$("button.answer").val("");
		}
	});
}

function add_questions(data) {
	var new_img1 = $("<img></img>").attr("src", "{{static_url(\"images/head/yy.png\")}}");
	var new_a1 = $("<a></a>").attr("href", "").append(new_img1);

	var new_span1 = $("<span></span>").text(data["userName"]).addClass("name");
	var new_img2 = $("<img></img>").addClass("if-cert").attr("src", "{{static_url(\"images/icon/have-cert.png\")}}");
	var new_btn1 = $("<button></button").text("+关注").addClass("btn btn-default");
	var new_span2 = $("<span></span>").addClass("care").append(new_btn1);
	var new_span3 = $("<span></span>").addClass("inform-coin").text(data["love_coin"] + " 爱心币");
	var new_p1 = $("<p></p>").append(new_span1, new_img2, new_span2, new_span3);

	var new_span4 = $("<span></span>").text(data["date"]);
	var new_p2 = $("<p></p>").append(new_span4);

	var new_div1 = $("<div></div>").addClass("header").append(new_a1, new_p1, new_p2);

	var new_p3 = $("<p></p>").text(data["content"]).addClass("text");

	var new_strong = $("<strong></strong>").text("标题:");
	var new_p4 = $("<p></p>").text(data["title"]).addClass("text-info").prepend(new_strong);

	var new_img4 = $("<img></img>").attr("src", "{{static_url(\"images/head/pml.jpg\")}}");
	var new_a2 = $("<a></a>").attr("href", "").append(new_img4);

	var new_p5 = $("<p></p>").text("PanMaolin:");
	var new_p6 = $("<p></p>").text("17:20");
	var new_div3 = $("<div></div>").addClass("comment-time").append(new_p5, new_p6);

	var new_p7 = $("<p></p>").text("谢谢");
	var new_div4 = $("<div></div>").addClass("comment-text").append(new_p7);

	var new_div5 = $("<div></div>").addClass("comment-piece").append(new_a2, new_div3, new_div4);

	var new_span6 = $("<span></span>").addClass("caret")
	var new_a3 = $("<a></a>").attr("href", "").text("更多评论").prepend(new_span6);
	var new_span5 = $("<span></span>").addClass("more-comment").append(new_a3);

	var new_div6 = $("<div></div>").addClass("old-comment").append(new_div5, new_span5);

	var new_img5 = $("<img></img>").attr("src", "{{static_url(\"images/button/comment.png\")}}");
	var new_div7 = $("<div></div>").addClass("comment-label").text(" 66条评论").prepend(new_img5);

	var new_input5 = $("<input></input>").addClass("form-control changewidth").attr("type", "text");
	var new_btn2 = $("<button></button").text("提交").addClass("btn btn-info answer").attr("type", "button");
	var new_span7 = $("<span></span>").addClass("input-group-btn closetoinput").append(new_btn2);
	var new_div8 = $("<div></div>").addClass("input-group").append(new_input5, new_span7);

	var new_div9 = $("<div></div>").addClass("comment").append(new_div7, new_div6, new_div8);

	var new_input6 = $("<input></input>").attr({"type": "hidden"}).val(data["eventId"]).addClass("event_id");
	var new_input7 = $("<input></input>").attr({"type": "hidden"}).val(data["id"]).addClass("launcher_id");
	var new_input8 = $("<input></input>").attr({"type": "hidden"}).val($("#user-id").val()).addClass("cuser_id");

	var new_div10 = $("<div></div>").addClass("piece").append(new_input6, new_input7, new_input8, new_div1, new_p4, new_p3, new_div9);

	var new_div11 = $("<div></div>").addClass("inform collapse in").append(new_div10);
	// alert($(new_div11).html());
	$("div.inform").append(new_div11);
	// $("#questionPiece").append(new_div11);
	// alert($("div.inform"));
	var id = $("#user-id").val();
    window.location.href = "/account";
}