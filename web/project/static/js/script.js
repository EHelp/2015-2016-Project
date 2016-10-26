$(document).ready(function() {

    //----------------------------------------
    //----FOR PAGE LOGIN.HTML--------------
    //----------------------------------------

    $("#button_login").click(function(check){
        check.preventDefault();

        var account_t = $("#account").val();
        var password_t = $("#password").val();
        var reg = new RegExp("^ +$");

        if (account_t == "" || password_t == "" || account_t.match(reg) || password_t.match(reg)) {

          alert("输入不能为空");
          return;
        }

        
        //to get the _xsrf cookies.
        var xsrf_t = getCookie("_xsrf");
        
        $.post("/account/get_salt_value", {account: account_t, _xsrf: xsrf_t},
            function(data,status){
              var salt = data;
              /*alert(salt)*/
              if (salt != "") {
                password_t = $.md5(password_t + salt);
                
                $.post("/account/login", {account: account_t, password:password_t, salt: salt, _xsrf: xsrf_t},
                  function(data,status){
                    var array = $.parseJSON(data);
                    if (array.status == 200) {
                      window.location.href = "/account";
                    } else {
                      alert("登陆失败，请再次尝试");
                    }
                  }
                );
              } else {
                //the salt is empty......
                alert("当前用户不存在");
              }
            }
        );
    });

    //-----------------------------------------
    //----FOR PAGE REGISTER
    //-----------------------------------------

    $("#iden_regist_button").click(function(check){
        check.preventDefault();
        var account_t = $("#account").val();
        var email_t = $("#email").val();
        var xsrf_t = getCookie("_xsrf");
        
        $.post("/account/get_iden_code", {account: account_t, email: email_t, _xsrf: xsrf_t},
            function(data, status) {
              var array = $.parseJSON(data);
              if (array.status == 200) {
                $("#secret").val(array.secret);
                alert("验证码已成功发送到您的邮箱");
              } else {
                if (array.status == 500) alert("验证码发送失败，请重新点击！");
                else alert("用户名已经被人注册！");
              }
        });
    });

    $("#button_regist").click(function(check){
        check.preventDefault();

        var account_t = $("#account").val();
        var password_t = $("#password").val();
        var email_t = $("#email").val();
        var phone_t = $("#phone").val();
        var identi_t = $("#identification").val();

        // alert($("#secret").val());

        // alert($.md5(account_t + identi_t + "?" + email_t));
        //to get the _xsrf cookies.
        var xsrf_t = getCookie("_xsrf");
        if ($.md5(account_t + identi_t + "?" + email_t) == $("#secret").val()) {
          $.post("/account/regist", {account:account_t, password: password_t, email: email_t, phone: phone_t, _xsrf: xsrf_t},
              function(data, status) {
                var dataArray = $.parseJSON(data);
                if (dataArray.status == 200) {
                  window.location.href = "/account/login";
                } else {
                  //注册失败，进行提示。
                  alert("注册失败");
                  window.location.href = "/account/regist";
                }
              }
          );
        } else {
          alert("验证码不正确！");
        }
    });

    //-----------------------------------------
    //----FOR PAGE FIND BACK PWD
    //-----------------------------------------

    $("#iden_button").click(function(check) {
        check.preventDefault();

        var account_t = $("#account").val();
        var email_t = $("#email").val();
        var xsrf_t = getCookie("_xsrf");
        $.post("/account/forget/ident", {account: account_t,email: email_t, _xsrf: xsrf_t},
            function(data,status){
              var array = $.parseJSON(data)
              if (array.status == 200) {
                $("#secret").val(array.secret);
                alert("the identification code is already sent to your email!");
              } else {
                //to indicate the errors......
                alert("the msg is not sended! please do it again!");
              }
            }
        );
    });

    $("#submit_button").click(function(check) {
      check.preventDefault();

      var account_t = $("#account").val();
      var identi_t = $("#identification").val();
      var secret_t = $("#secret").val();
      var xsrf_t = getCookie("_xsrf");
      //in fact, is equalivant to
      if (secret_t == $.md5(account_t + identi_t)) {
        var path= "?account="+account_t;
        window.location.href = "/account/setpwd" + path;
      } else {
        //to indicate the yanzhengma is wrong!
        alert("it does not match!!");
      }
    });

    $("#button_setpwd").click(function(check){
      check.preventDefault();
      //需要进行表单验证。
      var account_t = $("#account").val();
      var password_t = $("#password").val();
      var xsrf_t = getCookie("_xsrf");
      /*alert("test");*/
      $.post("/account/setpwd", {account: account_t, password: password_t, _xsrf: xsrf_t},
          function(data,status){
            var array = $.parseJSON(data)
            if (array.status == 200) {
              alert("密码修改成功！");
              window.location.href = "/account/login";
            } else {
              //to indicate the errors......
              alert("密码修改失败，请再次尝试！");
            }
          }
      );
    });


    $("#ui_form").validate({
      rules:{
        account:{
          required:true,
          minlength:11,
          maxlength:11
        },
        password:{
          required:true,
          minlength:6,
          maxlength:15
        },
        re_password:{
          equalTo:"#password"
        },
        email:{
          required:true,
          email:true
        },
        phone:{
          required:true,
          minlength:11,
          maxlength:11
        }
      },
      messages:{
        account:{
          required:"请填写11位手机号码",
          minlength:"请填写11位手机号码",
          maxlength:"请填写11位手机号码"
        },
        password:{
          required:"请填写6-15位密码",
          minlength:"密码最小为6位",
          maxlength:"密码最大为15位"
        },
        re_password:{
          equalTo:"两次输入的密码不一样"
        },
        email:{
          required:"请填写邮箱地址",
          email:"请输入正确的邮箱地址"
        },
        phone:{
          required:"请填写11位手机号码",
          minlength:"请填写11位手机号码",
          maxlength:"请填写11位手机号码"
        }
      }
    });




});

function getCookie(name) {
    
    //what 's cookie
    /*
    alert("------------------------------------");
    alert(typeof(document.cookie));
    alert(document.cookie);
    alert("--------------------------------------");
    */

    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    /*
    alert("--------------------------------------");
    alert(typeof(c));
    alert(c);

    alert("--------------------------------------"); 
    alert(typeof(c[1]));
    alert(c[1]);
    */
    return c ? c[1] : undefined;
}
