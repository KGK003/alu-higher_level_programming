#!/usr/bin/node
const $ = window.$;
$(document).ready(function () {
  $('#add_item').on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });
});
