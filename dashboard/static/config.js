// for tabbed content

function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].classList.remove("active");
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
    }
    document.getElementById(tabName).classList.add("active");
    evt.currentTarget.classList.add("active");
    localStorage.setItem("activeTab", tabName);
}

function closeBanner() {
    var banner = document.getElementById("success-banner");
    var header = document.querySelector(".header");
    banner.style.display = "none";
    header.style.marginTop = "0";
}

document.addEventListener("DOMContentLoaded", function() {
    var banner = document.getElementById("success-banner");
    var header = document.querySelector(".header");
    if (banner) {
        header.style.marginTop = "15px";
    }

    var activeTab = localStorage.getItem("activeTab");
    if (activeTab) {
        var tabcontent = document.getElementsByClassName("tabcontent");
        for (var i = 0; i < tabcontent.length; i++) {
            tabcontent[i].classList.remove("active");
        }
        var tablinks = document.getElementsByClassName("tablinks");
        for (var i = 0; i < tablinks.length; i++) {
            tablinks[i].classList.remove("active");
        }
        document.getElementById(activeTab).classList.add("active");
        document.querySelector(`.tablinks[onclick="openTab(event, '${activeTab}')"]`).classList.add("active");
    }
});