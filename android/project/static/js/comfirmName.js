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




	valid = $("#cert").validate({
		/*debug: true,*/
		rules: {
			realname: {
				minlength: 2,
				maxlength: 5,
				required: true
			},
			realID: {
				ifIdCard: true
			}
		},
		messages: {
			realname: {
				required: "请输入真实姓名",
				minlength: "姓名长度不少于2个字",
				maxlength: "姓名长度不多于5个字"
			}
		}
	});
	$.validator.addMethod("ifIdCard", function(value, element, params) {
		var factorArr = new Array(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,1);
		var parityBit=new Array("1","0","X","9","8","7","6","5","4","3","2");
		var varArray = new Array();
		var intValue;
		var lngProduct = 0;
		var intCheckDigit;
		var intStrLen = value.length;
		var idNumber = value;
		// initialize
		if ((intStrLen != 15) && (intStrLen != 18)) {
		return false;
		}
		// check and set value
		for(i=0;i<intStrLen;i++) {
		    varArray[i] = idNumber.charAt(i);
			if ((varArray[i] < '0' || varArray[i] > '9') && (i != 17)) {
				return false;
			}
			else if (i < 17) {
				varArray[i] = varArray[i] * factorArr[i];
			}
		}

		if (intStrLen == 18) {
			//check date
			// var date8 = idNumber.substring(6,14);
			// if (isDate8(date8) == false) {
			// 	return false;
			// }
			// calculate the sum of the products
			for(i=0;i<17;i++) {
				lngProduct = lngProduct + varArray[i];
			}
			// calculate the check digit
			intCheckDigit = parityBit[lngProduct % 11];
			// check last digit
			if (varArray[17] != intCheckDigit) {
				return false;
			}
		}
		else{ //length is 15
			//check date
			return false;
		}
		return true;
	}, "请输入正确身份证号码");
});


