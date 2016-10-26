$(document).ready(function() {
	$("#fb_send").click(function(check) {
		check.preventDefault();
		var title = $("#fb_title").val();
        var content = $("#fb_content").val();
        var contact = $("#fb_contact").val();
        var xsrf_t = getCookie("_xsrf");
        
        $.post("/aboutus", {title: title, content: content, contact: contact, _xsrf: xsrf_t},
            function(data, status) {
              var array = $.parseJSON(data);
              if (array.status == 200) {
                alert("您的反馈已成功发送！");
              } else {
              	alert("抱歉，您的反馈发送失败，请重试！");
              }
        });
	});
});

function getCookie(name) {
    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return c ? c[1] : undefined;
}
