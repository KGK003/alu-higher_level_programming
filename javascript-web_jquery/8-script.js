#!/usr/bin/node
const $ = window.$;
const fetchData = fetch('https://swapi-api.alx-tools.com/api/films/?format=json');
fetchData.then((res) => {
  return res.json();
}).then((data) => {
  data.results.forEach(element => {
    $('ul#list_movies').append(`<li>${element.title}</li>`);
  });
});
