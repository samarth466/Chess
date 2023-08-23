function delete_comment() {
    fetch("/delete-comment",{
        'method': 'DELETE'
    }).then(function (response) {
        if (response.ok) {
            return response.json();
        }
        return Promise.reject(response);
    }).then(function (data) {
        const msg = document.createElement("p");
        msg.innerText = data;
        document.body.appendChild(msg);
    }).catch(function (error) {
        const errorMsg = document.createElement("p");
        errorMsg.innerText = error;
        document.body.appendChild(errorMsg);
    });
};

const elements = document.getElementsByClassName("delete-comment");
for (let i = 0; i < elements.length; i++) {
    elements[i].onclick = delete_comment;
};
window.location.reload();