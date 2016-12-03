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
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue =   decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});