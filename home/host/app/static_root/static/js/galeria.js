
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
  var tam_slides = slides.length
  if(typeof slides[0] != "undefined"){
  var $section = document.querySelector(".bg-evento")
  $section.style.display = ""
  if (n > tam_slides) {slideIndex = 1}
  if (n < 1) {slideIndex = tam_slides}
  for (i = 0; i < tam_slides; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "inline-block";
  }
}