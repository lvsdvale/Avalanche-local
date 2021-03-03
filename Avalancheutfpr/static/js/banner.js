 var _index = 0;
 var timer;
    showSlide(_index);

    function set_slide(n){
        showSlide(_index = n)
    };

    function showSlide(n){

    var $slide = document.querySelectorAll(".banner .slide")
    var $pointer = document.querySelectorAll(".banner .sliders-pointers div")
    var $tam_slide = $slide.length

        for(var i=0;i<$tam_slide;i++){
             $slide[i].style.display= "none";
        }
        for (i = 0; i < $pointer.length; i++) {
        $pointer[i].className = $pointer[i].className.replace(" active", "");
        }
        if (_index >= $tam_slide) {_index = 0}
        $slide[_index].style.display = "block";
        $pointer[_index].className += " active";
        clearTimeout(timer);
        timer = setTimeout(() => set_slide(_index+1), 5000);

    }