const API_Key = "4377284227a3717fbedfa5ca18b3a692";
const BASE_URL = "https://api.themoviedb.org/3";

// https://api.themoviedb.org/3/movie/popular?api_key=YOUR_ACTUAL_API_KEY

export async function searchMovies(query){

    const res = await fetch(`${BASE_URL}/search/movie?api_key=${API_Key}&query=${query}`);

    const data = await res.json();
    return data.results;

}


export async function getTopMovies(){


     const res = await fetch(`${BASE_URL}/movie/popular?api_key=${API_Key}`);

    
    const data = await res.json();
    return data.results;
  
}