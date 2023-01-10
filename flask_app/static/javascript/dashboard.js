var count =12;

function press(){
    var p = document.querySelector("#count");
    count++;
    p.innerText = count + " likes";
    console.log(count);
}
press();
