#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  let characterRequests = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          return reject(error);
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  });

  Promise.all(characterRequests)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(err => {
      console.error('Error fetching character:', err);
    });
});
