const showmodal = document.querySelector(".show-modal")
const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay-all");
const closeModalBtn = document.querySelector(".btn-close");

// open modal event
if(showmodal){
    modal.setAttribute("style", "display:flex !important; top:50% !important;");
}

// close modal function
const closeModal = function(){
    modal.setAttribute("style", "display:none !important;");
    overlay.setAttribute("style", "display:none !important;");
};

// close the modal when the close button and overlay is clicked
if(closeModalBtn){
    closeModalBtn.addEventListener("click", closeModal);
}