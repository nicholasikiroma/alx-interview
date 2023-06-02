#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const filmId = process.argv[2];
  const filmUrl = `${API_URL}/films/${filmId}/`;

  request.get(filmUrl, (filmErr, filmRes, filmBody) => {
    if (filmErr) {
      console.error(filmErr);
      return;
    }

    const charactersURL = JSON.parse(filmBody).characters;
    const characterPromises = charactersURL.map(url => {
      return new Promise((resolve, reject) => {
        request.get(url, (charErr, charRes, charBody) => {
          if (charErr) {
            reject(charErr);
            return;
          }
          resolve(JSON.parse(charBody).name);
        });
      });
    });

    Promise.all(characterPromises)
      .then(names => {
        console.log(names.join('\n'));
      })
      .catch(allErr => {
        console.error(allErr);
      });
  });
}
