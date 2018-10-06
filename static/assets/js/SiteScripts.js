
   


$(document).on("click", ".MainNode", function () {
    var Div = $(this).closest(".SideTree");
    Div.children(".LeafNods").collapse("toggle");
    
    var Ps = require("perfect-scrollbar");
    var container = document.getElementByClass('SidebarContent');  //SidebarContentId
    Ps.update(container);
});

$(window).load(function () {
 /*  $(".SidebarContent").mCustomScrollbar({
        axis: "y",
        theme: "minimal"
    });*/
    $(".OverLayForm").mCustomScrollbar({
        axis: "y",
        theme: "inset-2-dark"
    });
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });
 
});


$(document).on("click", '[name="TaskeenType"]', function () {
    var TaskeenType = $(this).val();
    if (TaskeenType == 'change') {
        $("#travellerInput").collapse("show");
        $("#changeInput").collapse("show");
        $("#moveInput").collapse("hide");
    }else if (TaskeenType == 'move'){
        $("#travellerInput").collapse("show");
        $("#moveInput").collapse("show");
        $("#changeInput").collapse("hide");
    }
});

$(document).on("click", '[name="transportation_type"]', function () {
    var TripType = $(this).val();
    if (TripType == 'internal') {
        $("#in").collapse("show");
        $("#out").collapse("hide");
    }else if (TripType == 'external'){
        $("#out").collapse("show");
        $("#in").collapse("hide");
    }
});

$(document).on("click", '[name="flight_type"]', function () {
    var TripType = $(this).val();
    if (TripType == 'Wild') {
        $("#BusCompany").collapse("show");
        $("#FlightCompany").collapse("hide");
    }else if (TripType == 'flight'){
        $("#FlightCompany").collapse("show");
        $("#BusCompany").collapse("hide");
    }
});

$(document).on("click",' [name="RadioOppaytype"]', function () {
     var PaymentType = $(this).val();
    if (PaymentType == 'Cash') {
        $("#collapsePaymentType1").collapse("hide");
        $("#collapsePaymentType").collapse("hide");
    }else if (PaymentType == 'shick'){
        $("#collapsePaymentType").collapse("show");
        $("#collapsePaymentType1").collapse("hide");
    }else if (PaymentType == 'visacard'){
        $("#collapsePaymentType1").collapse("show");
        $("#collapsePaymentType").collapse("hide");
    }
});

$(document).on("click",' [name="RadioOpDaysafe"]', function () {
     var PaymentType = $(this).val();
    if (PaymentType == 'Day') {
        $("#from_toDiv").collapse("hide");
        $("#ActivityDiv").collapse("hide");
        $("#DayDiv").collapse("Show");
    }else if (PaymentType == 'from_to'){
        $("#ActivityDiv").collapse("hide");
        $("#DayDiv").collapse("hide");
        $("#from_toDiv").collapse("show");
    }else if (PaymentType == 'Activity'){
        $("#from_toDiv").collapse("hide");
        $("#DayDiv").collapse("hide");
        $("#ActivityDiv").collapse("show");
    }
});

$(document).on("click", '[name="ServicesTypeRadioOptions"]', function () {
    var TripType = $(this).val();
    if (TripType == 'Form') {
        $("#CustomerDiv").collapse("hide");
        $("#RoomDiv").collapse("hide");
        $("#FormDiv").collapse("show");
    }else if (TripType == 'Customer'){
        $("#FormDiv").collapse("hide");
        $("#RoomDiv").collapse("hide");
        $("#CustomerDiv").collapse("show"); 
    }else if (TripType == 'Room'){
        $("#CustomerDiv").collapse("hide");
        $("#FormDiv").collapse("hide");
        $("#RoomDiv").collapse("show"); 
    }
});

$(document).on("click", '[name="RadioOpDay0"]', function () {
    var TripType = $(this).val();
    if (TripType == 'Day') {
        $("#ActivityDiv").collapse("hide");
        $("#from_toDiv").collapse("hide");
        $("#DayDiv").collapse("show");
    }else if (TripType == 'from_to'){
        $("#ActivityDiv").collapse("hide");
        $("#DayDiv").collapse("hide");
        $("#from_toDiv").collapse("show"); 
    }else if (TripType == 'Activity'){
        $("#from_toDiv").collapse("hide");
        $("#DayDiv").collapse("hide");
        $("#ActivityDiv").collapse("show"); 
    }
});