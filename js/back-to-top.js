(function () {
  const btn = document.querySelector(".qiti-backtotop");
  if (!btn) return;

  const showAfterPx = 300;

  function toggle() {
    if (window.scrollY > showAfterPx) {
      btn.classList.add("is-visible");
    } else {
      btn.classList.remove("is-visible");
    }
  }

  window.addEventListener("scroll", toggle, { passive: true });
  toggle();

  btn.addEventListener("click", function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: "smooth" });
    // keep URL clean if you do not want #top
    history.replaceState(null, "", window.location.pathname + window.location.search);
  });
})();
