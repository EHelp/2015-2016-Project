var valid;
$(document).ready(function() {

	/*
	$("#modify_user").click(function(event) {
		event.preventDefault();
		id = $("#id").val();
		window.location.href = "/account/userinfo/modify/" + id;

	});

	$("#index").click(function(event) {

		event.preventDefault();
		id = $("#id").val();
		window.location.href = "/" + id;
	});
	*/




	 valid = $("#theEmail").validate({
		debug: true,
		rules: {
			newemail: {
				email: true,
				required: true
			}
		},
		messages: {
			newemail: {
				email: "请输入正确格式的邮箱地址",
				required: "请输入邮箱地址"
			}
		}
	});

/*----------------------------------------------------------*/
/*发送邮箱开始*/

	$("#sendNewEmail").click(function() {

		//event.preventDefault();
    	//alert("aaaaaaaaaaaaaaa");
		var id = $("#id").val();
		var email = $("#newemail").val();
	
		var xsrf_t = getCookie("_xsrf");
      
    	$.post("/account/userinfo/modify/email", {"id":id, "email": email, _xsrf: xsrf_t},  function(data, status) {
    		//window.location.href = "";

    		array = $.parseJSON(data);
    		if (array.status == 400) {
            
            	alert("还未进行密码验证，请进行");
    	   		window.location.href ="/account/userinfo/modify";
        	} else if (array.status == 500){

            	alert("操作失误， 重新尝试");
        	} else {

        		window.location.href = "/account/userinfo/modify/email_wait?email=" + email;
        	}
		});
    });

/*发送邮箱结束-----------------------------------------------*/
});


function getCookie(name) {
  
    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return c ? c[1] : undefined;
}


