 (function Menu(){
            'use strict';
    var $btn = document.getElementById("Bt_menu")
    var $nav = document.querySelector(".menu_nav")
    var $label = document.querySelector(".menu_label")
    var $submenuactiver = document.querySelector(".submenu_active")
    var $submenu = document.querySelector(".submenu")
    var _clicked = false;
    $btn.addEventListener('change', function(){
        if($btn.checked){
            $nav.style.display="flex";
            $nav.style.marginTop="10px";
            $label.innerHTML = "&#9747";
            $label.style.fontSize = "45px";
            }
        else{
            $nav.style.display="none";
            $label.innerHTML = "&#9776";
            $label.style.fontSize = "40px";
            }
    });
    window.addEventListener("resize",function(){
        if(window.innerWidth>800){
            $nav.style.display="block";
        }
        else{
            $nav.style.display="none";

        }
    }
    )
    if(window.innerWidth<800){
        $submenuactiver.addEventListener("click",function(){
                if(_clicked){
                    $submenu.style.visibility = "hidden";
                    $submenu.style.display= "none";
                    $submenu.style.position = "absolute";
                    _clicked = false;
                }
                else{
                $submenu.style.visibility ="visible";
                $submenu.style.display= "block";
                $submenu.style.position = "static";
                _clicked = true;
                }
            }
        )
    }
    })()