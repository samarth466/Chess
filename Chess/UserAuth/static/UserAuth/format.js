function format() {
    var fields = document.getElementsByTagName('input')
    document.getElementById('#id_day').id = 'day'
    var formRect = document.getElementById('#form').getBoundingClientRect();
    var elemRect = document.getElementById('#day').getBoundingClientRect();
    var topPosition = elemRect.top - formRect.top;
    var row = document.createElement("tr");
    var i;
    for (i = 0; i < fields.length(); i ++){
        if(fields[i].name==='id_day'){
            row.appendChild(fields[i]);
        };
    };
    row.top = topPosition;
};
window.onload = format();