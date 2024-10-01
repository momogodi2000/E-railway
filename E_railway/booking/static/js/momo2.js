document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
    const dashboardNav = document.querySelector(".dashboard-nav");
    const dashboardApp = document.querySelector(".dashboard-app");
    const dashboardToolbar = document.querySelector(".dashboard-toolbar");

    menuToggle.addEventListener("click", function () {
        dashboardNav.classList.toggle("closed");
        dashboardApp.classList.toggle("closed");
    });

    dashboardNav.addEventListener("transitionend", () => {
        if (dashboardNav.classList.contains("closed")) {
            dashboardToolbar.classList.add("closed");
        } else {
            dashboardToolbar.classList.remove("closed");
        }
    });
});