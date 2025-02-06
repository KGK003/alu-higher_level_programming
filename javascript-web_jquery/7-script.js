#!/usr/bin/node
const $ = window.$;
const fetchData = fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json');
fetchData.then((res) => {
  return res.json();
}).then((data) => {
  $('div#character').text(data.name);
});
