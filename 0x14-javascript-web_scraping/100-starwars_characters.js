#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (let i = 0; i < characters.length; i++) {
    const character = characters[i];
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      const dataChar = JSON.parse(body);
      const name = dataChar.name;
      console.log(name);
    });
  }
});
