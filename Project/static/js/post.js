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

function resetFileInput() {
    var fileInput = document.getElementById("fileInput");
    fileInput.value = "";

    var previewImage = document.getElementById("preview");
    previewImage.src = "";
}

function readImage(input) {
    // 인풋 태그에 파일이 있는 경우
    if(input.files && input.files[0]) {
        // 이미지 파일인지 검사 (생략)
        // FileReader 인스턴스 생성
        const reader = new FileReader()
        // 이미지가 로드가 된 경우
        reader.onload = e => {
            const previewImage = document.getElementById("preview")
            previewImage.src = e.target.result
        }
        // reader가 이미지 읽도록 하기
        reader.readAsDataURL(input.files[0])
    }
}
// input file에 change 이벤트 부여
const inputImage = document.getElementById("fileInput")
inputImage.addEventListener("change", e => {
    readImage(e.target)
})
