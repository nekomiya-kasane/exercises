import axios from "axios";

export const getSearchMovie = async(name,year,pageNumber)=>{
    try{
        const res = await axios.get(`http://sefdb02.qut.edu.au:3000/movies/search?title=${name??''}&year=${year??''}&page=${pageNumber??''}`)
        return res.data
    } catch {
        throw new Error('SearchMoiveError');
    }

}

export const getMovieInfo = async(id)=>{
    try{
        const res = await axios.get(`http://sefdb02.qut.edu.au:3000/movies/data/${id}`)
        return res.data
    } catch {
        throw new Error('getMovieInfoError');
    }
}

