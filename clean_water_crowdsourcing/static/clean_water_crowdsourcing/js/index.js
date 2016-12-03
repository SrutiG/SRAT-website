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
    $("#submit-purity-nav").click(function() {
            $(".submit-purity-report").show();
            $(".main").css("opacity", 0.3);
    })
    $("#cancel-purity-report").click(function() {
        $(".submit-purity-report").hide();
        $(".main").css("opacity", 1);
    })
    $("#cancel-source-report").click(function() {
            $(".submit-source-report").hide();
            $(".main").css("opacity", 1);
    })
    $("#edit-profile-nav").click(function() {
            $(".edit-profile").show();
            $(".main").css("opacity", 0.3);
    })
    $("#cancel-edit-profile").click(function() {
        $(".edit-profile").hide();
        $(".main").css("opacity", 1);
    })
});