#!/usr/bin/env node
/*
 * This script prints all characters of a Star Wars movie
 */

const request = require('request');

const args = process.argv.slice(2);
if (args.length !== 1) {
  console.log('Usage: 0-starwars_characters.js <filmID>');
  process.exit(1);
}
const filmID = args[0];

request(`https://swapi-api.alx-tools.com/api/films/${filmID}`,
  function (err, res, body) {
    if (!err) {
      res = JSON.parse(body);
      res.characters.forEach(url => {
        request(url, function (err, res, body) {
          if (!err) {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  });
