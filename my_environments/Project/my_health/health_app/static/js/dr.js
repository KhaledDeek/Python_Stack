$(document).ready(function () {
    $("#form").on('submit', function (event) {
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCSRFToken()
            }
        });
        $.ajax({
            type: 'POST',
            url: '/ptinfo',
            data: {
                national_id: $("#national_id").val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        })
    })
});