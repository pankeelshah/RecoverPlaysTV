function clicked(){
    console.log("Clicked the button");
    document.getElementById("showLoading").innerHTML = '<div class="spinner-border"></div>';
    var username = document.querySelector("#username").value;
    console.log(username);
    var url = '/proxy/download/' + username;
    let promise = fetch(encodeURI(url));
    let jr = promise.then(function(resp){
        console.log("going in");
        return resp.json();
    })
    jr.then( 
        function(data){
            console.log(data);
            document.getElementById("downloadBtn").disabled = false;
            document.getElementById("showLoading").innerHTML = "";
        }
    )
}