var socket = io("//");
var username;

socket.on('message', data => {
  var downloadStatus = document.getElementById("downloadStatus");
  downloadStatus.innerHTML = data;
});

socket.on('downloadComplete', elem => {
  document.getElementById("downloadButton").disabled = false;
  document.getElementById("searchButton").disabled = false;
});

function clickedSearch(){
  username = document.getElementById("username").value;

  if(username == ""){
    alert("Please enter a username.")
    return
  }

  document.getElementById("downloadButton").disabled = true;
  document.getElementById("searchButton").disabled = true;
  socket.emit("download", username);
}

function clickedDownload(){
  window.open("/" + username + ".zip");
}

// Press enter to search
window.onload = function(){ 
  document.getElementById("username").onkeypress=function(e){
      if(e.keyCode==13){
          document.getElementById("searchButton").click();
      }
  }
};