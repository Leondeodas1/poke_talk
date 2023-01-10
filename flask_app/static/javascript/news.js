thisis = document.querySelector("#char")

var currentUsername = "";

function search(element) {
    console.log(element.value);
    currentUsername = element.value;
}
function makecodercard(data) {  
    var res = `<div id="char" style= "border-style: solid;height:100px;width:100%;border-radius: 5%;padding: 10px;">
                    <button"><a href="${data.articles[0].url}" >${data.articles[0].title}</a></button>
                    <p style="font-size: small;">Published At: ${data.articles[0].publishedAt}</p>
                </div>`
    return res;
}


async function show() {
    var response = await fetch("https://newsapi.org/v2/everything?q=" + currentUsername + "&from=2023-01-08&language=en&apiKey=0375043b8cca4d68a40e18b5f6df8f8b");
    var coderData = await response.json();
    console.log(coderData);
    thisis.innerHTML = makecodercard(coderData);
}
