import React, { useEffect, useState } from 'react';
import { useParams ,useNavigate} from 'react-router-dom';
import { Table,message,Spin ,Typography} from 'antd';
import { Link } from 'react-router-dom';
import { getPeopleInfo } from '../api/userAPI';
import ReactEcharts from 'echarts-for-react';

const columns = [
  {
	title: 'Movie Name',
	dataIndex: 'movieName',
	key: 'movieName',
	render: (text, record) => (
	  <Link to={`/moviePage/${record.movieId}`}>{text}</Link>
	),
  },
  {
	title: 'Category',
	dataIndex: 'category',
	key: 'category',
  },
  {
	title: 'IMDb Rating',
	dataIndex: 'imdbRating',
	key: 'imdbRating',
  },
];
const RatingsChart = ({ data }) => {
	const option = {
	  title: {
		text:'IMDB ratings at a glance'
	  },
	  tooltip: {
		trigger: 'axis',
		axisPointer: {
		  type: 'shadow',
		},
	  },
	  xAxis: {
		type: 'category',
		data: [...Array(11).keys()],
		axisLabel: {
		  formatter: (value, index) => {
			if (index === 0) {
			  return '<1';
			} else if (index === 10) {
			  return '10+';
			} else {
			  return `${value}-${parseInt(value)+1}`;
			}
		  },
		},
	  },
	  yAxis: {
		type: 'value',
	  },
	  series: [
		{
		  data: data,
		  type: 'bar',
		},
	  ],
	};
  
	return <ReactEcharts option={option} />;
  };
  
const StarInfo = (starInfo) => {
	const { name, birthYear, deathYear, roles } = starInfo.star
	const dataSource = roles.map((role) => ({ ...role, key: role.movieId }));

	const birthDeathText = deathYear
	? `${birthYear} - ${deathYear}`
	: `${birthYear} - `;

	const ratingData = Array(11).fill(0);
	roles.forEach((role) => {
	  const rating = Math.floor(role.imdbRating);
	  if (rating < 1) {
		ratingData[0]++;
	  } else if (rating > 10) {
		ratingData[10]++;
	  } else {
		ratingData[rating]++;
	  }
	});
	return (
	<div>
		<h1>{name}</h1>
		<h3>{birthDeathText}</h3>
		<Table dataSource={dataSource} columns={columns} />
		<RatingsChart data={ratingData}/>
	</div>
	);
};


const StarPage = () => {
	const { id } = useParams();
	const [starInfo,setStarInfo]= useState()
	const [loggedIn, setLoggedIn] = useState(null);
	const navigate = useNavigate();
	const [flag,setFlag]=useState(false)
	function checkLoginStatus() {
		const loginInfo = localStorage.getItem('loginInfo');
		if (loginInfo) {
			const token = JSON.parse(localStorage.getItem('loginInfo'));
			if (token && token.bearerTokenexpirationTime > Date.now()) {
				// valid login info, return token
				return token;
			} else {
				// expired login info, remove from local storage
				localStorage.removeItem('loginInfo');
			}
		}
		// no valid login info found
		return null;
	}

	useEffect(() => {
		const login = checkLoginStatus();
		if (login) {
		  setLoggedIn(login);
		} else {
		  message.warning('You are not logged in.');
		  navigate('/user')
		}
	}, [navigate]);

	// Check login status every 5 seconds
	useEffect(() => {
		const intervalId = setInterval(() => {
			const login = checkLoginStatus();
			if (!login) {
				setLoggedIn(null);
				message.warning('You are not logged in.');
				navigate('/user');
			}
		}, 5000);

		return () => clearInterval(intervalId);
	}, [navigate]);

	useEffect(()=>{
		if(loggedIn!=null){
			getPeopleInfo(id,loggedIn.bearerToken.token).then(setStarInfo).catch(()=>setFlag(true))
		}
	},[id,loggedIn])

    useEffect(()=>{
      if(flag) {
        message.error("Movie Not Found")
      }
    },[flag])
	return (
		loggedIn != null && starInfo ?  
		<StarInfo star={starInfo}/>:
		<div style={{ textAlign: 'center', marginTop: '2rem' }}>
			{
				flag?<div style={{ textAlign: 'center', marginTop: '2rem' }}>
				<Typography.Title type="danger">people Not Found</Typography.Title>
				</div>:<Spin size="large" />
			}
		</div>
	);
  };

export default StarPage;
