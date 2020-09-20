
    var slideIndex = 1;
     showSlides(slideIndex);
function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.querySelectorAll(".section-evento-area .slide");
  if(typeof slides[0] != "undefined"){
  var $title = document.querySelector(".section-evento-area .section-title")
  var $previous = document.querySelector(".previous")
  var $nextslide = document.querySelector(".nextslide")
  $title.style.display = ""
  $nextslide.style.display = ""
  $previous.style.display = ""
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "inline-block";
  }
}