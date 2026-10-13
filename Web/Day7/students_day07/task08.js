const items = document.querySelectorAll('a:not([target="_blank"])');
items.forEach((item) => {
  item.style.opacity = "0.5";
});