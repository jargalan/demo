$(document).ready(function(){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $("#btn_new").click(function(){
        $(this).hide();
        $("#form_add").slideDown();
    });

    $("#btn_cancel").click(function(){
        $("#btn_new").show();
        $("#form_add").slideUp();
    });

    $("#btn_search").click(function(){
        $("#tbl_app tbody").html("");
        $.ajax({
            type: "POST",
            url: "/list",
            data: {'keyword': $("#txt_keyword").val()},
            dataType: 'json',
            success: function(data) {
                if(data.list.length == 0) {
                    var td = $("<td/>", {'colspan':3}).text("No appointments are available.");
                    $('<tr/>').append(td).appendTo("#tbl_app tbody");
                    return;
                }
                for(var i=0; i<data.list.length; i++) {
                    var td1 = $("<td/>").text(data.list[i]['date']);
                    var td2 = $("<td/>").text(data.list[i]['time']);
                    var td3 = $("<td/>").text(data.list[i]['description']);
                    $('<tr/>').append(td1, td2, td3).appendTo("#tbl_app tbody");
                }
            }
        });
    });

    $('#txt_keyword').keypress(function(e) {
        if (e.which == 13) {
            $("#btn_search").trigger("click");
        }
    });

    $("#btn_search").trigger("click");
});