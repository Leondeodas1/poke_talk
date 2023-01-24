thisis = document.querySelector("#char")

var currentUsername = "";

function search(element) {
    console.log(element.value);
    currentUsername = element.value;
}
function makecodercard(data) {
    var res = `
    <div id="char" style= "border-style: solid;height:100px;width:100%;border-radius: 5%;padding: 10px;">
                    <button"><a href="${data.articles[0].url}" >${data.articles[0].title}</a></button>
                    <p style="font-size: small;">Published At: ${data.articles[0].publishedAt}</p>
                    <p style="font-size: small;">Published At: </p>
                </div>
                
            <div style= "border-style: solid;height:100px;width:100%;border-radius: 5%;padding: 10px;">
                <button"><a href="${data.articles[1].url}" >${data.articles[1].title}</a></button>
                <p style="font-size: small;">Published At: ${data.articles[1].publishedAt}</p>
                <p style="font-size: small;">Published At: </p>
            </div>
            
        <div style= "border-style: solid;height:100px;width:100%;border-radius: 5%;padding: 10px;">
            <button"><a href="${data.articles[2].url}" >${data.articles[2].title}</a></button>
            <p style="font-size: small;">Published At: ${data.articles[2].publishedAt}</p>
            <p style="font-size: small;">Published At: </p>
        </div>

        <div style= "border-style: solid;height:100px;width:100%;border-radius: 5%;padding: 10px;">
            <button"><a href="${data.articles[3].url}" >${data.articles[3].title}</a></button>
            <p style="font-size: small;">Published At: ${data.articles[3].publishedAt}</p>
            <p style="font-size: small;">Published At: </p>
        </div>
            
        <div style= "border-style: solid;height:100px;width:100%;border-radius: 5%;padding: 10px;">
            <button"><a href="${data.articles[4].url}" >${data.articles[4].title}</a></button>
            <p style="font-size: small;">Published At: ${data.articles[4].publishedAt}</p>
            <p style="font-size: small;">Published At: </p>
        </div>`
                console.log(data.articles)
    return res;
}


async function show() {
    var response = await fetch("https://newsapi.org/v2/everything?q=" + currentUsername + "&from=2023-01-08&apiKey=0375043b8cca4d68a40e18b5f6df8f8b");
    var coderData = await response.json();
    thisis.innerHTML = makecodercard(coderData);
}
  


fetch("https://newsapi.org/v2/everything?q=pokemon&from=2023-01-08&apiKey=0375043b8cca4d68a40e18b5f6df8f8b").then((data)=>{
    // console.log(data)
    return data.json();  
}).then((objectData)=>{
    console.log(objectData.articles[0].author);
    let tableData ="";
    objectData.articles.map((values)=>{
        tableData+=`  <table class="table table-bordered" style="height: 10px;">

        <tbody id="table_body"  style= "border-style: solid;height:100px;width:100%;border-radius: 5%;padding: 10px;">
          <tr style="height: 10px;> 
          <button"><a href="${values.url}" >${values.title}</a></button>
            <p style="height: 10px;>${values.title}</p>
            <p style="height: 10px;>${values.publishedAt}</p>
          </tr>
        </tbody>
      </table>
</div>   ;`; 
    });
    extreme = document.querySelector("#table_body")
        extreme.innerHTML=tableData;
        console.log(tableData)
})
            
            