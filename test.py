$(document).ready(function() {
    $("#preview").click(function() {

        // Get the modal
        var modal = document.getElementById('myModal');

        // Get the button that opens the modal
        var btn = document.getElementById("preview");

        // Get the <span> element that closes the modal
        var span = document.getElementsByClassName("close")[0];

        // When the user clicks the button, open the modal 
        /*btn.onclick = function() */
        {
            modal.style.display = "block";
        }

        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
            modal.style.display = "none";
        }

        //file logic (installation)
        var lang = document.getElementById("language").value;
        var keyboard = document.getElementById("keyboard").value;
        var timezone = document.getElementById("timezone").value;	
	var pass = document.getElementById("repass").value;
	var target = document.getElementById("target_architecture").value;
	var firstboot = document.getElementById("first-boot").value;

	if(document.getElementById("utc_check").checked == true){
		finaltimezone = timezone;
	}
	else{
		finaltimezone = timezone+"--isUtc";
	}
	
	if(document.getElementById("reboot".checked == true){
		reboot = "# Reboot after installation<br/>reboot";
	}
	else{
		reboot = "# Halt after installation<br/>halt";
	}

	if(document.getElementById("textmode").checked == true){
		textmode = "# Use text mode install<br/>text";
	}
	else{
		textmode = "# Use graphical install<br/>graphical";
	}

	if(document.getElementById("display_checkbox").checked == true){
		finalfirstboot = "# Run the Setup Agent on first boot<br/>firstboot "+firstboot;		
	}
	else{
		finalfirstboot = "# Run the Setup Agent on first boot<br/>firstboot --reconfig<br/># Do not configure the X Window System<br/>skipx";
	}

	$("#addcontent").append("#platform="+target+"<br/># Keyboard layouts<br/>keyboard '"+keyboard+"'<br/># System language<br/>"+lang+"<br/># System timezone<br/>"+finaltimezone+"<br/># Root password<br/>rootpw "+pass+"<br/>"+reboot+"<br/>"+textmode+"<br/>"+finalfirstboot+"<br/>");
	



        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    });
});
