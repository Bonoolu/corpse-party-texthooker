let pattern = /.*Sound:.*]/;
setInterval(function() {
    let textbox = document.querySelector('#search-textbox');
    if (textbox.value.match(pattern)) {
        textbox.value = textbox.value.replace(pattern, "");
        let search = document.querySelector('#search-button');
        search.click();
    }
}, 200);