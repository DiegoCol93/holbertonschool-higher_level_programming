const $ = window.$;
const fetch = window.fetch;

async function filmsList (url) {
  const response = await fetch(url);
  const dict = await response.json();

  // For Each movie in the results Object
  dict.results.forEach((result) => {
    // Apend the title of the result.
    $('UL#list_movies').append($('<li>' + result.title + '</li>'));
  });
}

filmsList('https://swapi-api.hbtn.io/api/films/?format=json');
