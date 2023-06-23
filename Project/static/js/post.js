var track_btn_1 = document.getElementById("track_btn_1");
var track_btn_2 = document.getElementById("track_btn_2");
var track_btn_3 = document.getElementById("track_btn_3");
var track_btn_4 = document.getElementById("track_btn_4");
var track_btn_5 = document.getElementById("track_btn_5");
var track_btn_6 = document.getElementById("track_btn_6");
var track_btn_7 = document.getElementById("track_btn_7");
var track_btn_8 = document.getElementById("track_btn_8");

var field_btn_1 = document.getElementById("field_btn_1");
var field_btn_2 = document.getElementById("field_btn_2");
var field_btn_3 = document.getElementById("field_btn_3");
var field_btn_4 = document.getElementById("field_btn_4");


changeBackgroundColor(track_btn_1);
changeBackgroundColor(track_btn_2);
changeBackgroundColor(track_btn_3);
changeBackgroundColor(track_btn_4);
changeBackgroundColor(track_btn_5);
changeBackgroundColor(track_btn_6);
changeBackgroundColor(track_btn_7);
changeBackgroundColor(track_btn_8);

changeBackgroundColor(field_btn_1);
changeBackgroundColor(field_btn_2);
changeBackgroundColor(field_btn_3);
changeBackgroundColor(field_btn_4);

function changeBackgroundColor(button) {
    var clickCount = 0;

    button.addEventListener("click", function() {
    if (clickCount % 2 === 0) {
        button.style.backgroundColor = "#66C081";
        button.style.color = "white";
    } else {
        button.style.backgroundColor = "#D9D9D9";
        button.style.color = "#747474";
    }
    clickCount++;
    });
}  

