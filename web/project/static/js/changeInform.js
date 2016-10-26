var valid;
$(document).ready(function() {
	$(".handset").bind("click", function() {
		$('body,html').animate({scrollTop:0},1000);
	});
	$(".email").bind("click", function() {
		$('body,html').animate({scrollTop:400},1000);
	});
	$(".password").bind("click", function() {
		$('body,html').animate({scrollTop:820},1000);
	});
	$(".real-name").bind("click", function() {
		$('body,html').animate({scrollTop:1250},1000);
	});
	$(".information").bind("click", function() {
		$('body,html').animate({scrollTop:1600},1000);
	});
	valid = $("#changePassword").validate({
		debug: true,
		rules: {
			nowpassword: {
				minlength: 4,
				maxlength: 16,
				required: true
			},
			newpassword: {
				minlength: 4,
				maxlength: 16,
				required: true
			},
			"comfirmpassword": {
				equalTo: "#newpassword"
			}
		},
		messages: {
			nowpassword: {
				minlength: "请保持密码长度为4-16位",
				maxlength: "请保持密码长度为4-16位",
				required: "请输入原密码"
			},
			newpassword: {
				minlength: "请保持密码长度为4-16位",
				maxlength: "请保持密码长度为4-16位",
				required: "请输入新密码"
			},
			"comfirmpassword": {
				equalTo: "两次输入密码不一致"
			}
		}
	});

	/*是否已经验证*/


	var isVerified = parseInt($(".is-verified").val());

	/*alert(isVerified);*/
	if (!isVerified) {
		
        $("#hadntComfirm").show();  // 单词拼写错误了
        $("#hadComfirm").hide();
	} else {

		$("#hadComfirm").show();
        $("#hadntComfirm").hide();
	}

/*--------------------------------------------------------------*/
/*对电话修改进行密码确认*/
/*--------------------------------------------------------------*/
	$("#sendPassword").click(function() {

	//to get the _xsrf cookies.
    var xsrf_t = getCookie("_xsrf");

    var password = $(".form-now-password").val();
    var id = parseInt($(".id").val());

    
    $.post("/account/get_salt_value", {"id":id, _xsrf: xsrf_t}, function(salt, status) {
 		
            //alert("here-----------------------------");
            //alert(salt);

    		password = $.md5(password + salt);  // 加密方法语法不知道有没有错误，加上同一个函数里面使用了data代表两个不同的数
    		$.post("/account/passwordVerify", {"id":id, "password" : password, _xsrf: xsrf_t}, function(data,status) {
    			var data = $.parseJSON(data);
    			if (data.status == 400) {
    				$(".wrong-password").show();
    				//alert("密码错误");
    			}
    			else if (data.status == 500) {
    				alert("操作失败，请再次提交。");
    			}
    			else if (data.status == 200) {
                    window.location.href = "/account/userinfo/modify/phone";
    			}
    		});
   
    });
});

/*对电话修密码确认完成--------------------------------*/



/*----------------------------------------------------*/
/*对邮箱进行密码确认*/
/*----------------------------------------------------*/


	$("#sendPasswordForEmail").click(function() {

	//to get the _xsrf cookies.
    var xsrf_t = getCookie("_xsrf");

    var password = $("#nowpasswordForEmail").val();
    var id = parseInt($(".id").val());

    
    $.post("/account/get_salt_value", {"id":id, _xsrf: xsrf_t}, function(salt, status) {
 		
            //alert("here-----------------------------");
            //alert(salt);

    		password = $.md5(password + salt);  // 加密方法语法不知道有没有错误，加上同一个函数里面使用了data代表两个不同的数
    		$.post("/account/passwordVerify", {"id":id, "password" : password, _xsrf: xsrf_t}, function(data,status) {
    			var data = $.parseJSON(data);
    			if (data.status == 400) {
    				//$(".wrong-password").show();
    				alert("密码错误");
    			}
    			else if (data.status == 500) {
    				alert("操作失败，请再次提交。");
    			}
    			else if (data.status == 200) {
                    window.location.href = "/account/userinfo/modify/email";
    			}
    		});
   
    });
});




/*--邮箱密码确认完成--------------------------------------------------------*/



/*--------------------------------------------------------------------------*/
/*跳转实名认证*/
/*-------------------------------------------------------------------------*/

	$("#real_name_comfire").click(function() {

		var id = $(".id").val();
		window.location.href = "/account/userinfo/modify/real_name_comfirm";

	});


/*--跳转实名认证完成--------------------------------------------------------*/




});


function getCookie(name) {
  
    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return c ? c[1] : undefined;
}