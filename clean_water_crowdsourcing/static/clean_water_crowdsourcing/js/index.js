$(document).ready(function() {
    $("#cancelBT").click(function() {
        parent.history.back();
        return false;
    });
    $("#submit-source-nav").click(function() {
        $(".submit-source-report").show();
        $(".main").css("opacity", 0.3);
    })
    $("#cancel-source-report").click(function() {
        $(".submit-source-report").hide();
        $(".main").css("opacity", 1);
    })
});