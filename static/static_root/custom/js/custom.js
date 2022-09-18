const formSubmit = () => {
    console.log('Working...');
}

// Get the Scroll button
let mybutton = document.getElementById("scrollBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    console.log(document.documentElement.scrollTop);
    if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
        mybutton.style.display = "block";
    }
    else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction(props) {
    console.log(props);
    if (props === 'home') {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }
    else if (props === 'service') {
        document.body.scrollTop = 635;
        document.documentElement.scrollTop = 635;
    }
    else if (props === 'portfolio') {
        document.body.scrollTop = 1240;
        document.documentElement.scrollTop = 1240;
    }
    else if (props === 'about') {
        document.body.scrollTop = 2035;
        document.documentElement.scrollTop = 2035;
    }
    else if (props === 'testmonial') {
        document.body.scrollTop = 3995;
        document.documentElement.scrollTop = 3995;
    }
    else if (props === 'contact') {
        document.body.scrollTop = 6250;
        document.documentElement.scrollTop = 6250;
    }
    // document.body.scrollTop = 1240;
    // document.documentElement.scrollTop = 1240;
}

// 

const aboutSection = () => {
    document.documentElement.scrollTop = 0;
}