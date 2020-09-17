 (function Menu(){
            'use strict';
    var $btn = document.getElementById("Bt_menu")
    var $nav = document.querySelector(".menu_nav")
    var $label = document.querySelector(".menu_label")
    $btn.addEventListener('change', function(){
    if($btn.checked){
    $nav.style.display="flex";
    $nav.style.marginTop="10px";
    $label.innerHTML = "&#9747"
    $label.fontSize = "25px"
    }
    else{
    $nav.style.display="none";
    $label.innerHTML = "&#9776"
    }

    });
    })()