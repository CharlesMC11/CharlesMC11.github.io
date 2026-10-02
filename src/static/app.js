function initScrollToTop() {
  const scrollBtn = document.querySelector(".scroll-to-top");
  if (!scrollBtn) return;

  window.addEventListener(
    "scroll",
    () => {
      if (window.scrollY > 256) {
        scrollBtn.classList.add("visible");
      } else {
        scrollBtn.classList.remove("visible");
      }
    },
    {passive: true},
  );

  scrollBtn.addEventListener("click", (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initScrollToTop()
})
