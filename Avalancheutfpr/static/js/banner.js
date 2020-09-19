 var _index = 0;
    showSlide();
    function showSlide(){
    var $slide = document.querySelectorAll(".banner .slide")
    var $pointer = document.querySelectorAll(".banner .sliders-pointers div")
        for(var i=0;i<$slide.length;i++){
             $slide[i].style.display= "none";
        }
        _index++;
        if (_index > $slide.length) {_index = 1}
        for (i = 0; i < $pointer.length; i++) {
        $pointer[i].className = $pointer[i].className.replace(" active", "");
        }
        $slide[_index-1].style.display = "block";
        $pointer[_index-1].className += " active";
        setTimeout(showSlide, 3000);
    }