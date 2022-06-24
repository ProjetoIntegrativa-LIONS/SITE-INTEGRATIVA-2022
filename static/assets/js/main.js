
let fixed= true;
const header = document.querySelector("header");

window.addEventListener("scroll", function(event) {

    if(this.scrollY > 80){
        header.classList.toggle("fixed", true);
        return
    }
    
    header.classList.toggle("fixed", false);
    
});





// let show = true;

// const header = document.querySelector("header");
// const menuSection = document.querySelector("header");
// const menuToggle = document.querySelector(".menu-toggle");

// menuToggle.addEventListener("click", () => {
//     document.body.style.overflow = show ? "hidden" : "initial"
//     menuSection.classList.toggle("on", show);
//     show = !show;
// })
    