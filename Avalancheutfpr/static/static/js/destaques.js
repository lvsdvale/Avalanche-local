    var slideIndex = 1;
    showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.querySelectorAll(".section-premium .slide");
  var tam_slides = slides.length
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = tam_slides}
  for (i = 0; i < tam_slides; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "inline-block";
}