function clicked(){
    console.log("Clicked the button");
    var url = '/proxy/download';
    let promise = fetch(encodeURI(url));
    let jr = promise.then(function(resp){
        console.log("going in")
        return resp.json();
    })
    jr.then( 
        function(data){
            console.log(data);
        }
    )
}