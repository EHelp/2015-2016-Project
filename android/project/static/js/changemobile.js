var valid;
var wait = 60;
function time(o, p) {
	if (wait == -1) {
		o.removeAttr("disabled");
		o.text("点击发送验证码");
		p.html("如果您在1分钟内没有收到验证码，请检查您填写的手机号码是否正确或重新发送");
		wait = 60;
	} else {
		o.attr("disabled", true);
		o.text(wait + "秒后重新获取验证码");
		wait--;
		setTimeout(function() {
			time(o, p);
		}, 1000);
	}
}
$(document).ready(function() {


	/*
	$("#modify_user").click(function(event) {
		event.preventDefault();
		id = $(".id").val();
		window.location.href = "/account/userinfo/modify/" + id;

	});
	*/


	/*
	$("#index").click(function(event) {

		event.preventDefault();
		id = $(".id").val();
		window.location.href = "/" + id;
	});
	*/



	valid = $("#phoneNumber").validate({
		debug: true,
		rules: {
			newphone: {
				minlength: 11,
				maxlength: 11,
				digits: true,
				required: true
			}
		},
		messages: {
			newphone: {
				required: "请输入新手机号码", //  建议这里的样式改成红色小一点的字
				minlength: "请输入正确长度的手机号码",
				maxlength: "请输入正确长度的手机号码",
				digits: "请输入正确格式的手机号码"
			}
		}
	});

	/*
	$("#getComID").click(function() {
		time($(this), $("#submitComID"));
	})*/

	

	$("#getComID").click(function() {

    time($(this), $("#submitComID"));

	var id = $(".id").val();
	var account = $(".account").val();
	var email = $(".email").val();
	var xsrf_t = getCookie("_xsrf");

	//alert(account);
	//alert(email);
    
    email = email.replace("%40", "@");
    //alert(email);

    $.post("/account/userinfo/modify/get/idenCode", {"account": account, "email": email, _xsrf: xsrf_t},  function(data, status) {
    	array = $.parseJSON(data);
    	if (array.status == 200) {
            
            $("#secret").val(array.secret);
            alert("验证码已成功发送到您的邮箱");
        
        } else {
            if (array.status == 500) alert("验证码发送失败，请重新点击！");
            
        }
    });
});

$(".ensure").click(function() {
	var id = $(".id").val();
    var secret = $("#secret").val();    
    var account_t = $(".account").val();
    var email_t = $(".email").val();
    var identi_t = $("#comID").val();
    var phone = $("#newphone").val();
    //to get the _xsrf cookies.
    var xsrf_t = getCookie("_xsrf");
    email_t = email_t.replace("%40", "@");
    //alert(email_t);

    if ($.md5(account_t + identi_t + "?" + email_t) == $("#secret").val()) {
         $.post("/account/userinfo/modify/phone", {"id": id, "phone": phone, _xsrf: xsrf_t},
                  function(params, status) {
            
            data = $.parseJSON(params);

    		if (data.status == 500) {
    			alert("操作失败，请重新尝试");
    		}
    	   	else if (data.status == 400){
    	   		alert("还未进行密码验证，请进行");
    	   		window.location.href ="/account/userinfo/modify";
    			
    		} else {
    			window.location.href = "/account/userinfo/modify/phone/success";
    		}
             
          });

    } else {

    	alert("验证码不正确");
    }
    

});

});



function getCookie(name) {
  
    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return c ? c[1] : undefined;
}


