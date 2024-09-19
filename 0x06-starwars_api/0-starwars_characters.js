#!/usr/bin/node
import fetch from 'node-fetch';

async function getMovieCharacters(movieId) {
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

    try {
        const movieResponse = await fetch(movieUrl);
        if (!movieResponse.ok) {
            throw new Error(`Error: Received status code ${movieResponse.status}`);
        }

        const movieData = await movieResponse.json();
        console.log(`Characters in '${movieData.title}':\n`);

        for (const characterUrl of movieData.characters) {
            const characterResponse = await fetch(characterUrl);
            const characterData = await characterResponse.json();
            console.log(characterData.name);
        }
    } catch (error) {
        console.error(`Error fetching data: ${error.message}`);
    }
}

const movieId = process.argv[2];
if (!movieId) {
    console.error('Usage: node 0-starwars_characters.js <Movie ID>');
} else {
    getMovieCharacters(movieId);
}
