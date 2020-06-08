function clicked(){
    document.getElementById("searchButton").disabled = true;
    document.getElementById("showLoading").innerHTML = '<div class="spinner-border"></div>';

    var username = document.querySelector("#username").value;
    var url = '/proxy/download/' + username;
    let promise = fetch(encodeURI(url));

    let jr = promise.then(function(resp){
        return resp.json();
    })
    jr.then( 
        function(data){
            window.open('/static/' + username + '_PlaysTVClips.zip');
            document.getElementById("searchButton").disabled = false;
            document.getElementById("showLoading").innerHTML = "";
        }
    )
}