function styling() {
    const heading = document.querySelector('h1').innerHTML
    const msg = "The passwords do not match. Try again."
    if(heading === msg){
        const bold = document.createElement('strong');
        bold.innerHTML = msg;
    };
};

document.addEventListener('DOMContentLoaded',styling)