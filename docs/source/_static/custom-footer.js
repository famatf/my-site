document.addEventListener("DOMContentLoaded", function () {
  const bottom = document.querySelector(".bottom-of-page");
  if (!bottom) return;

  const indexLink = document.querySelector('link[rel="index"]');
  const indexHref = indexLink ? indexLink.getAttribute("href") : "genindex.html";
  const root = indexHref.replace("genindex.html", "");

  const links = document.createElement("div");
  links.className = "custom-footer-links";
  links.innerHTML = `
    <a href="${root}about.html">关于本站</a>
    ·
    <a href="https://github.com/famatf">GitHub</a>
  `;

  bottom.appendChild(links);
});