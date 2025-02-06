#!/usr/bin/node
const $ = window.$;
const fetchData = fetch('https://fourtonfish.com/hellosalut/?lang=fr');
fetchData.then((res) => {
  console.log(res.json());
  return res.json();
}).then((data) => {
  $('div#hello').append(data.hello);
});
