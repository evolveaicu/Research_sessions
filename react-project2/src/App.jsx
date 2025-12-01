import {useState , useEffect } from "react";
import { searchMovies , getTopMovies } from "./api";
import MovieCard  from "./MovieCard";
import "./css/styles.css";



function App() {

  const [query , setQuery] = useState("");

  const [movies , setMovies ] = useState([]);


  useEffect(()=>{ 

    async function loadTopMovies(){

      const top = await getTopMovies();
    
      setMovies(top);
      
    }
    loadTopMovies();
  }, []);


  async function handleSearch(e){

    e.preventDefault();
    
    if(!query.trim()) return;


    const results = await 
    searchMovies(query);
    setMovies(results);


  }

  return (

    <div className ="app">
      <h1>Movie Search App</h1>

      <form onSubmit={handleSearch}>
        <input type="text"
        
        placeholder="Search for movies ......"

        value = {query}

        onChange = {(e) => setQuery(e.target.value)}
        
        />
        <button type="Submit">Search</button>

      </form>

      <div className="movie-grid">

        {

          movies.map((m) => (

            <MovieCard key={m.id} movie = {m}/>
          )
        
        
        )
        }
      </div>



      
    </div>

  );




}

export default App;