import React from 'react';
import { Typography ,Image} from 'antd';
import Search from '../assets/Search.jpg'

function Home() {
  return (
    <div style={{display:'flex',flexDirection:'column',alignItems:'center'}}>
      <Typography.Title >Yuxuan Wang's Fabulous Movie Searching Website</Typography.Title>
      <Image alt={"Movie Search poster"} height={500} width={1000} preview={false} src={Search}/>
      <Typography>I hope you find the movie you're after!</Typography>
      <Typography>All data is from IMDB, Metacritic and RottenTomatoes. © 2023 Yuxuan Wang</Typography>
    </div>
  );
}

export default Home;
