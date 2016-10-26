$(document).ready(function() {


	/*alert("aaaa");*/
	$("#sendEmail").click(function(event) {

		/*alert("aaaa");*/
		var id = $("#id").val();
		var email = $("#email").val();
		var xsrf_t = getCookie("_xsrf");

		// alert(email);
		$.post("/account/userinfo/modify/email", {"id": id, "email": email, "_xsrf":xsrf_t},
			function(data, status) {

				// alert(data);
				array = $.parseJSON(data);
				if (array.status == 200) {
					alert("email is send please wait");
				} else {

					alert("error");
				}
			});
	});

});


function getCookie(name) {
  
    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return c ? c[1] : undefined;
}



