const axios = require("axios");

async function getMovieCharacters(movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  try {
    const movieResponse = await axios.get(movieUrl);
    const movieData = movieResponse.data;

    console.log(`Characters in '${movieData.title}':\n`);

    // Fetch all character data concurrently
    const characterPromises = movieData.characters.map((characterUrl) =>
      axios.get(characterUrl)
    );
    const characterResponses = await Promise.all(characterPromises);

    // Print all character names
    characterResponses.forEach((characterResponse) => {
      const characterData = characterResponse.data;
      console.log(characterData.name);
    });
  } catch (error) {
    console.error(`Error fetching data: ${error.message}`);
  }
}

const movieId = process.argv[2];
if (!movieId) {
  console.error("Usage: node script.js <Movie ID>");
} else {
  getMovieCharacters(movieId);
}
