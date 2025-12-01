
function MovieCard({ movie }){
    return(


        <div className = "movie-card">
        
        <img src ={`https://image.tmdb.org/t/p/w500${movie.poster_path}`}
          
          alt = {movie.title}
          />

          <h2>{movie.title}</h2>

        </div>

    );
}

export default MovieCard;