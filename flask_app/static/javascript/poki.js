thisis = document.querySelector("#char")
my = document.querySelector("#hi")
console.log(my.innerText);

var currentUsername = my.innerText;

function makecodercard(data) { 
    var res = `<div class="card">
                    <img src="${data.sprites.back_shiny}" alt="${data.sprites.back_shiny}" style="width:100px; height: 100px;">
                    <img src="${data.sprites.front_shiny}" alt="${data.sprites.front_shiny}" style="width:100px; height: 100px;">
                    <h3>${data.name} - ${data.species}</h3>
                    <p>height: ${data.height}</p>
                    <p>weight: ${data.weight}</p>
                    <p>species: ${data.species.url}</p>
                    <p>Ability Name: ${data.abilities['0'].ability.name}</p>
                </div>`
    return res;
} 

async function show(element) {
    var response = await fetch("https://pokeapi.co/api/v2/pokemon/" + currentUsername);
    var coderData = await response.json();
    console.log(coderData);
    thisis.innerHTML = makecodercard(coderData);
    element.remove();
}

// async function find() {
//     var response = await fetch("https://api.twitter.com/2/users/by/username/$iamcardib Authorization: Bearer $1421664083510763522-KEoUEJyeXevc1qIS9vmuYvgcOOU0Fs");
//     var coderData = await response.json();
//     console.log(coderData);
//     thisis.innerHTML = makecodercard(coderData);
// }