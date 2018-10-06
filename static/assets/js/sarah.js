
$(document).on("click", "#hideNot", function () {

//alert($(this).data('employee-id'));
    var data = {
        employeeid: $(this).data('employee-id'),
        dealid: $(this).data('msg-id')

    }

    $.post("<? php echo $this->config->base_url(); ?>employee/readMsg", data, function (result) {
    });

});