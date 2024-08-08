#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data, status) {
  const titles = data.results;
  titles.forEach((movie) => {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
