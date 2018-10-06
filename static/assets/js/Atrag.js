var toggle = true;
            
$(".sidebar-icon").click(function() {                
  if (toggle)
  {
    $(".page-container").addClass("sidebar-collapsed").removeClass("sidebar-collapsed-back");
    $("#menu span").css({"position":"absolute"});
  }
  else
  {
    $(".page-container").removeClass("sidebar-collapsed").addClass("sidebar-collapsed-back");
    setTimeout(function() {
      $("#menu span").css({"position":"relative"});
    }, 400);
  }
                
                toggle = !toggle;
            });
			
		//---------------------------DatePicker--------
 $(document).on("click", ".SubItemBtnOpen", function ()
    {
        $(this).closest("td").children(".SubItem").collapse('toggle');
    });
	//----------------------
	$("#emp_id").change(function ()	
	{
		var idCard = document.getElementById("emp_id");
		
		var idYeargenerate = (idCard.value).slice(0,1);
		
		var country_i = (idCard.value).slice(7,9);
		
		var idYear = (idCard.value).slice(1,3);
		
		var idMonth = (idCard.value).slice(3,5);
		
		var idDay = (idCard.value).slice(5,7);
		
		var idGender = (idCard.value).slice(12,13);

		var dataroot = document.getElementById("emp_birthdate");
		
		var Gendercheck = $("input[name='RadioOp:Gender0']:checked");
	
		if( idYeargenerate == 2 ){
			

			dataroot.value = "19" + idYear +  "-" + idMonth + "-" + idDay  ;
			
		} 
        else {
			
            dataroot.value = "20" + idYear +  "-" + idMonth + "-" + idDay  ;			
		}
	if ( idGender % 2 == 0 ){
			
			$("#inlineRadio2egp").prop('checked',true);
	}
	else{
			$("#inlineRadio1egp").prop('checked',true);
	}
	
	
	});
	
	
	
	
$(document).ready(function() {
$('#password').keyup(function() {
$('#result').html(checkStrength($('#password').val()))
})
function checkStrength(password) {
var strength = 0
if (password.length < 6) {
$('#result').removeClass()
$('#result').addClass('short')
return 'Too short'
}
if (password.length > 7) strength += 1
// If password contains both lower and uppercase characters, increase strength value.
if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) strength += 1
// If it has numbers and characters, increase strength value.
if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/)) strength += 1
// If it has one special character, increase strength value.
if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
// If it has two special characters, increase strength value.
if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
// Calculated strength value, we can return messages
// If value is less than 2
if (strength < 2) {
$('#result').removeClass()
$('#result').addClass('weak')
return 'Weak'
} else if (strength == 2) {
$('#result').removeClass()
$('#result').addClass('good')
return 'Good'
} else {
$('#result').removeClass()
$('#result').addClass('strong')
return 'Strong'
}
}
});