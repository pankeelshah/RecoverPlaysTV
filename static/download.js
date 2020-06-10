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
            // deleteZip(username);
        }
    )
}

function deleteZip(username){
    var url = '/proxy/deletezip/' + username;
    let promise = fetch(encodeURI(url));
    let jr = promise.then(function(resp){
        return resp.json();
    })
    jr.then( 
        function(data){
            // console.log("")
        }
    )
}

window.onload = function(){ 
    document.getElementById("username").onkeypress=function(e){
        if(e.keyCode==13){
            document.getElementById("searchButton").click();
        }
    }
};

// var socket = io();
// var status = 0;
// socket.on('connect', function() {
//     socket.emit('my event', {data: 'I\'m connected!'});
// });

// socket.on('message', function(msg) {
//     document.getElementById("stat").innerHTML = msg;
// });