document.addEventListener(onload,function(){
    const link = document.getElementById('#login-with-google');
    const url = '/google/get-auth-url';
    fetch(url)
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        link.href = data.url
    })
});