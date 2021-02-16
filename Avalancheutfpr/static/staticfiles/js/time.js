    var $team = document.querySelectorAll(".Section-team .slide");
    function teamDisplay(){
    if(window.innerWidth>900){
    $team[1].style.display = "inline-block";
    $team[2].style.display = "inline-block";
        }
    if(window.innerWidth<900 && window.innerWidth>640){
    $team[1].style.display = "inline-block";
    $team[2].style.display = "none";
        }
    if(window.innerWidth<=640){
    $team[2].style.display = "none";
    $team[1].style.display = "none";
        }
    }
    teamDisplay();
    window.addEventListener("resize",function(){
        teamDisplay();
        })
