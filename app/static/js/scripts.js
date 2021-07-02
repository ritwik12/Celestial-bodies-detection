console.log("Hello from scripts.js!"); 
function upload_image() {
    // show loading gif when processing
    console.log("uploading");
    var x = document.getElementsByClassName("loader");
    var i;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "block";
    }
    var x = document.getElementsByClassName("my-image-form");
    var i;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
}

function open_browser(){
    // open file browser
    $('#image_file').trigger('click'); 
}

function hide_know_more(){
    // when no button is clicked
    $("#know_more")[0].style.display="none";
}

$(document).ready(function(){
    $("input[type=file]").on('change',function(){
        // when file selected
        document.getElementById("image_url").value="";
        document.getElementById("imageName").style.display = "block";
        // document.getElementById("imageName").style.color = "white";
        document.getElementById("imageName").innerText = this.files[0].name;
    });
});