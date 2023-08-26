import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Typography, List, Tag, Image,Spin, Divider, message } from 'antd';
import { getMovieInfo } from '../api/movieAPI';
import { Link } from 'react-router-dom';


const { Title, Text } = Typography;

const MovieIntroPage = ({ movie }) => {
  const { poster, runtime, year, genres, country, ratings, plot, principals } = movie;
  const imdbRating = ratings.find(({ source }) => source === 'Internet Movie Database')?.value;
  const tomatoMeter = ratings.find(({ source }) => source === 'Rotten Tomatoes')?.value;
  const metascore = ratings.find(({ source }) => source === 'Metacritic')?.value;

  const tagColors = ['magenta', 'volcano', 'orange', 'gold', 'green', 'cyan', 'blue', 'geekblue', 'purple'];

  const genreTags = genres.map((genre, index) => {
      const color = tagColors[index % tagColors.length];
      return <Tag color={color}>{genre}</Tag>;
  });

  const infoItems = [
    { title: 'Released Year', content: year },
    { title: 'Movie Time', content: `${runtime} min` },
    { title: 'Genre', content: genreTags },
    { title: 'Country', content: country },
    imdbRating && { title: 'IMDb', content: `${imdbRating} /10` },
    tomatoMeter && { title: 'Rotten Tomatoes', content: `${tomatoMeter}%` },
    metascore && { title: 'Metascore', content: `${metascore} / 100` },
    { title: 'Description',content:plot}
  ].filter(Boolean);

  return (
    <div style={{display:'flex',flexDirection:'row',justifyContent:'space-evenly'}}>
      <div>
        <Image alt={"Movie Poster"} src={poster} style={{width:'30vw',padding:'5px'}}/>
      </div>
      <div>
        <Title level={2} >{movie.title}</Title>
        <List
          itemLayout="horizontal"
          dataSource={infoItems}
          renderItem={({ title, content }) => (
            <List.Item>
              <Text strong>{title}: </Text>
              <Text>{content}</Text>
            </List.Item>
          )}
        />
        <Divider />
        <List
          itemLayout="horizontal"
          dataSource={principals}
          renderItem={({ name, category, characters, id }) => (
            <List.Item>
              <List.Item.Meta
                title={<Link to={`/people/${id}`} style={{color:'blue'}}>{name}</Link>}
                description={`Role: ${category}`}
              />
              <Text>{characters.join(', ')}</Text>
            </List.Item>
          )}
          pagination={false}
        />
      </div>
    </div>
  );
};

function MoviePage() {
    const { id } = useParams();
    const [movieInfo,setMovieInfo]=useState()
    const [flag,setFlag] = useState(false)
    useEffect(()=>{
      if(id) {
        getMovieInfo(id).then(setMovieInfo).catch(()=>{
          setFlag(true)
        })
      }
    },[id])
    useEffect(()=>{
      if(flag) {
        message.error("Movie Not Found")
      }
    },[flag])
    return (
      flag? 
      <div style={{ textAlign: 'center', marginTop: '2rem' }}>
        <Typography.Title type="danger">Movie Not Found</Typography.Title>
      </div>:
        movieInfo ? <MovieIntroPage movie={movieInfo} />:<div style={{ textAlign: 'center', marginTop: '2rem' }}>
        <Spin size="large" />
      </div>
    );
}

export default MoviePage;
