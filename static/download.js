var id;
var socket = io.connect('http://' + document.domain + ':' + location.port);
var status = 0;
var username;

function clicked(){
    document.getElementById("searchButton").disabled = true;
    document.getElementById("showLoading").innerHTML = '<div class="spinner-border"></div>';

    username = document.querySelector("#username").value;
    console.log(id);
    socket.emit("createzip", {user: username, sid:id})
    // var url = '/proxy/download/' + username + '/' + id;
    // let promise = fetch(encodeURI(url));

    // let jr = promise.then(function(resp){
    //     return resp.json();
    // })
    // jr.then( 
    //     function(data){
    //         window.open('/static/' + username + '_PlaysTVClips.zip');
    //         document.getElementById("searchButton").disabled = false;
    //         document.getElementById("showLoading").innerHTML = "";
    //         // deleteZip(username);
    //     }
    // )
}


function deleteZip(username){
    var url = '/proxy/deletezip/' + username  + '/' + id;
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

socket.on('connect', function() {
    id = socket.io.engine.id;
    // console.log(id);
    socket.emit('my event', {data: 'I\'m connected!'});
});


socket.on('message', function(msg) {
    // console.log(msg)
    // if(msg == "created-zip"){
    //     console.log(msg);
        
    // }else{
        document.getElementById("stat").innerHTML = msg;
    // }
    
});


socket.on("created-zip", function(username){
    window.open('/static/' + username + '_PlaysTVClips.zip');
    document.getElementById("searchButton").disabled = false;
    document.getElementById("showLoading").innerHTML = "";
})

