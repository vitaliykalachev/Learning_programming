

//function myFunction() {
//  var txt;
//  if (confirm("Press a button!")) {
//    txt = "You pressed OK!";
//  } else {
//    txt = "You pressed Cancel!";
//  }
//  document.getElementById("demo").innerHTML = txt;
//}


//
//if (confirm("Press a button!")) {
//  txt = "You pressed OK!";
//} else {
//  txt = "You pressed Cancel!";
//}
//myFunction()

function confirmBooking(elem) {
        if(confirm('Are you sure you want to book this slot?') == true) {
            //elem = 1;
            alert("its done: " + elem);
            document.getElementById("userInput").value = "True";
        }
        else {
             document.getElementById("userInput").value = "False";
             return 0;
        }
    }

//window.confirm("Сохраняю?");