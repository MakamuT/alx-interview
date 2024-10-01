#!/usr/bin/node
const request = require('request');

function getMovieCharacters(movieId) {
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

    request(movieUrl, (error, response, body) => {
        if (error) {
            console.error(`Error fetching movie data: ${error.message}`);
            return;
        }

        if (response.statusCode !== 200) {
            console.error(`Error: Received status code ${response.statusCode}`);
            return;
        }

        const movieData = JSON.parse(body);
        console.log(`Characters in '${movieData.title}':\n`);

        movieData.characters.forEach((characterUrl) => {
            
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error(`Error fetching character data: ${error.message}`);
                    return;
                }

                if (response.statusCode !== 200) {
                    console.error(`Error: Received status code ${response.statusCode}`);
                    return;
                }

            
                const characterData = JSON.parse(body);
                console.log(characterData.name);
            });
        });
    });
}

const movieId = process.argv[2];
if (!movieId) {
    console.error('Usage: node 0-starwars_characters.js <Movie ID>');
} else {
    getMovieCharacters(movieId);
}

