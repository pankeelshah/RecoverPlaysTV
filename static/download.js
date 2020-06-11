var id;
var socket = io.connect('http://' + document.domain + ':' + location.port);
var status = 0;
var username;

function clicked(){
    document.getElementById("searchButton").disabled = true;
    document.getElementById("showLoading").innerHTML = '<div class="spinner-border"></div>';
    username = document.querySelector("#username").value;
    socket.emit("createzip", {user: username, sid:id})
    console.log(username + ":" + id);
}

// Press enter to search
window.onload = function(){ 
    document.getElementById("username").onkeypress=function(e){
        if(e.keyCode==13){
            document.getElementById("searchButton").click();
        }
    }
};

// Get id when client connects
socket.on('connect', function() {
    id = socket.io.engine.id;
    
    socket.emit('my event', {data: 'I\'m connected!'});
});

socket.on('message', function(msg) {
    document.getElementById("stat").innerHTML = msg;   
});

socket.on("created-zip", function(username){
    window.open('/static/' + username + '_PlaysTVClips.zip');
    document.getElementById("searchButton").disabled = false;
    document.getElementById("showLoading").innerHTML = "";
    socket.emit("deletezip", {user: username, sid:id})
})



