$(document).ready(function() {

    init();

	$(".circle").click(changeColor);
    
    $("select").change(changePo);

	$(".delete").click(delRel);
});

function changeColor() {
	$(this).addClass("circleClick").siblings().removeClass("circleClick");
	
    $("." + $(this).attr("id")).show();

	for (var i = 0; i < $(this).parent().children().not(this).length; i++) 
        $("." + $($(this).parent().children().not(this)[i]).attr("id")).hide();
}

function init() {

	$("#family").addClass("circleClick");

    $(".family").show();
    $(".family").siblings().hide();

}

function delRel() {
    if (confirm("确定将该联系人删除吗？")) {
        var nickname = $(this).parent().parent().children(":first").text();
        var that = this;
        $.post("/account/manageRelationship/delete", {"nickname": nickname}, function(data, status) {

            var array = $.parseJSON(data);
            if (array.status == 200) {

                $(that).parent().parent().remove();
            } else {

                alert("操作出错 请重新尝试");
            }

        });
    }
}

function changePo(event) {

    // alert("aaa");
    event.preventDefault();
    var currentPosition = $(this).parent().parent().parent().parent().parent().attr("class");
    var whereToPlace = $(this).val();
    var data = $(this).parent().parent();
    var nickname = $(this).parent().parent().children(":first").text();

    // var temp = $(this).html();

    var type = 0;
    var temp = "家人";
    if (whereToPlace == "relatives") {
        type = 2
        temp = "亲朋";
    } else if (whereToPlace == "neighbour") {
        type = 1;
        temp = "邻居";
    }
    
    if (confirm("确定将该联系人移动到" + temp + "吗？")) {  //  将使用那种通过key直接访问的形式进行更加人性化，但是目前并不知道怎样写
        
        var that = this;
        $.post("/account/manageRelationship/update", {"type": type, "nickname": nickname}, function(dataCome, status) {

            var array = $.parseJSON(dataCome);
            if (array.status == 200) {

                $(that).parent().parent().remove();
                $($("." + whereToPlace).find("tbody")).append(data);
                // data.change(changePo);
                $($("." + whereToPlace).find("tbody")).find("select").unbind();
                $($("." + whereToPlace).find("tbody")).find("select").change(changePo);
            } else {

                alert("操作出错 请重新尝试");
            }
        });

        
    } else {

        $(this).unbind("change");
        $(this).val(currentPosition);
        // $(this).change(changePo);
    }
    $(this).change(changePo);
    $(".delete").click(delRel);
}