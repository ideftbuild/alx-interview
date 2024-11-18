#!/usr/bin/node
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

function fetchUrl (url) {
  return new Promise((resolve, reject) => {
    request({ url, json: true }, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function fetchCharacters (url) {
  try {
    // Fetch the film data
    const filmData = await fetchUrl(url);

    // Fetch characters sequentially to maintain order
    for (const characterUrl of filmData.characters) {
      const character = await fetchUrl(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchCharacters(`https://swapi-api.alx-tools.com/api/films/${filmID}`);
