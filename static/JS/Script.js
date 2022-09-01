const navbar = document.querySelector('.navParent');

window.addEventListener('scroll', ()=> {
    const winScroll = window.pageYOffset;
    console.log(navbar.classList);
    if (winScroll > 50){
        navbar.classList.remove('navParentDeactive');
        navbar.classList.add('navParentActive');
    }else{
        navbar.classList.remove('navParentActive');
        navbar.classList.add('navParentDeactive');
    }
})