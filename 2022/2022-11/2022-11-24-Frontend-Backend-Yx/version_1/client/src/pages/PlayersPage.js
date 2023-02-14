import React from 'react';
import { Form, FormInput, FormGroup, Button, Card, CardBody, CardTitle, Progress } from "shards-react";

import {
    Table,
    Pagination,
    Select,
    Row,
    Col,
    Divider,
    Slider,
    Rate 
} from 'antd'
import { RadarChart } from 'react-vis';
import { format } from 'd3-format';




import MenuBar from '../components/MenuBar';
import { getPlayer, getPlayerCompare, getWinningRate } from '../fetcher'
const wideFormat = format('.3r');

const playerColumns = [
    {
        title: 'Name',
        dataIndex: 'PLAYER_NAME',
        key: 'PLAYER_NAME',
        sorter: (a, b) => a.PLAYER_NAME.localeCompare(b.PLAYER_NAME),
        // render: (text, row) => <a href={`/players?id=${row.PLAYER_ID}`}>{text}</a>
    },
    {
        title: 'ID',
        dataIndex: 'PLAYER_ID',
        key: 'PLAYER_ID',
        sorter: (a, b) => a.PLAYER_ID.localeCompare(b.PLAYER_ID)
    },
    {
        title: 'Team',
        dataIndex: 'TEAM_ID',
        key: 'TEAM_ID',
        sorter: (a, b) => a.TEAM_ID - b.TEAM_ID

    },
    {
        title: 'Season',
        dataIndex: 'SEASON',
        key: 'SEASON',
        sorter: (a, b) => a.SEASON - b.SEASON

    },

];

const rateColumns = [
    {
        title: 'Season',
        dataIndex: 'SEASON',
        key: 'SEASON',
        sorter: (a, b) => a.SEASON - b.SEASON,
        // render: (text, row) => <a href={`/players?id=${row.PLAYER_ID}`}>{text}</a>
    },
    {
        title: 'Winning Rate',
        dataIndex: 'winning_rate',
        key: 'winning_rate',
        sorter: (a, b) => a.winning_rate - b.winning_rate
    }
];

const compareColumns = [
    {
        title: 'Season',
        dataIndex: 'SEASON',
        key: 'SEASON',
        sorter: (a, b) => a.SEASON.localeCompare(b.SEASON),
    },
    {
        title: '# Games',
        dataIndex: 'N_GAMES',
        key: 'N_GAMES',
        sorter: (a, b) => a.N_GAMES.localeCompare(b.N_GAMES)
    },
    {
        title: 'Player A Wins',
        dataIndex: 'N_GAMES_A_WINS',
        key: 'N_GAMES_A_WINS',
        sorter: (a, b) => a.N_GAMES_A_WINS - b.N_GAMES_A_WINS

    },
    {
        title: 'Player B Wins',
        dataIndex: 'N_GAMES_B_WINS',
        key: 'N_GAMES_B_WINS',
        sorter: (a, b) => a.N_GAMES_B_WINS - b.N_GAMES_B_WINS

    },

];


class PlayersPage extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            playerIDQuery:'',
            playersResults: [],
            playerAIDQuery:'',
            playerBIDQuery:'',
            compareResults: [],
            rateQuery: '',
            rateResults: []
        }

        this.updateSearchResults = this.updateSearchResults.bind(this)
        this.handlePlayerIDQueryChange = this.handlePlayerIDQueryChange.bind(this)

        this.updateRateResults = this.updateRateResults.bind(this)
        this.handleRateQueryChange = this.handleRateQueryChange.bind(this)
        
        this.handlePlayerAIDQueryChange = this.handlePlayerAIDQueryChange.bind(this)
        this.handlePlayerBIDQueryChange = this.handlePlayerBIDQueryChange.bind(this)
        this.updateCompareResults = this.updateCompareResults.bind(this)
    }

    handlePlayerIDQueryChange(event) {
        this.setState({ playerIDQuery: event.target.value })
    }

    updateSearchResults() {
        // console.log(`Running updateSearchResults() for playerIDQuery ${this.state.playerIDQuery}...`)
        getPlayer(this.state.playerIDQuery).then(res => {
            this.setState({ playersResults: res.results })
        })

        // console.log(this.state.playersResults);
    }

    handleRateQueryChange(event) {
        this.setState({rateQuery: event.target.value})
    }

    updateRateResults() {
        getWinningRate(this.state.rateQuery).then(res => {
            this.setState({ rateResults: res.results })
        })
    }

    handlePlayerAIDQueryChange(event) {
        this.setState({ playerAIDQuery: event.target.value })
    }

    handlePlayerBIDQueryChange(event) {
        this.setState({ playerBIDQuery: event.target.value })
    }

    updateCompareResults() {
        getPlayerCompare(this.state.playerAIDQuery, this.state.playerBIDQuery).then(res => {
            this.setState({ compareResults: res.results })
        })
    }

    // componentDidMount() {
    //     if (this.state.playerIDQuery > 0) {
    //         getPlayer(this.state.playerIDQuery).then(res => {
    //             this.setState({ selectedPlayerDetails: res.results[0] })
    //             console.log(res.results);
    //         })    
    //     }
    // }

    render() {
        return (

            <div>

                <MenuBar />
                <Form style={{ width: '80vw', margin: '0 auto', marginTop: '5vh' }}>
                    <Row>
                        <Col flex={2}><FormGroup style={{ width: '20vw', margin: '0 auto' }}>
                            <label>Player ID</label>
                            <FormInput placeholder="Player ID" value={this.state.playerIDQuery} onChange={this.handlePlayerIDQueryChange} />
                        </FormGroup></Col>

                        <Col flex={2}><FormGroup style={{ width: '10vw' }}>
                            <Button style={{ marginTop: '4vh' }} onClick={this.updateSearchResults}>Search</Button>
                        </FormGroup></Col>
                    </Row>
                    <br></br>
                </Form>

                <Divider />

                <div style={{ width: '70vw', margin: '0 auto', marginTop: '2vh' }}>
                <Table dataSource={this.state.playersResults} columns={playerColumns} pagination={{ pageSizeOptions:[5, 10], defaultPageSize: 5, showQuickJumper:true }}/>
                </div>

                <Divider />

                <Form style={{ width: '80vw', margin: '0 auto', marginTop: '5vh' }}>
                    <Row>
                        <Col flex={2}><FormGroup style={{ width: '20vw', margin: '0 auto' }}>
                            <label>Team Name</label>
                            <FormInput placeholder="Team Name" value={this.state.rateQuery} onChange={this.handleRateQueryChange} />
                        </FormGroup></Col>

                        <Col flex={2}><FormGroup style={{ width: '10vw' }}>
                            <Button style={{ marginTop: '4vh' }} onClick={this.updateRateResults}>Search</Button>
                        </FormGroup></Col>
                    </Row>
                    <br></br>
                </Form>

                <Divider />

                <div style={{ width: '70vw', margin: '0 auto', marginTop: '2vh' }}>
                <Table dataSource={this.state.rateResults} columns={rateColumns} pagination={{ pageSizeOptions:[5, 10], defaultPageSize: 5, showQuickJumper:true }}/>
                </div>

                <Divider />

                <Row>
                    <Col flex={2}><FormGroup style={{ width: '20vw', margin: '0 auto' }}>
                        <label>Player A</label>
                        <FormInput placeholder="Player A ID" value={this.state.playerAIDQuery} onChange={this.handlePlayerAIDQueryChange} />
                    </FormGroup></Col>

                    <Col flex={2}><FormGroup style={{ width: '20vw', margin: '0 auto' }}>
                        <label>Player B</label>
                        <FormInput placeholder="Player B ID" value={this.state.playerBIDQuery} onChange={this.handlePlayerBIDQueryChange} />
                    </FormGroup></Col>

                    <Col flex={2}><FormGroup style={{ width: '10vw' }}>
                        <Button style={{ marginTop: '4vh' }} onClick={this.updateCompareResults}>Compare</Button>
                    </FormGroup></Col>
                </Row>

                <div style={{ width: '70vw', margin: '0 auto', marginTop: '2vh' }}>
                <Table dataSource={this.state.compareResults} columns={compareColumns} pagination={{ pageSizeOptions:[5, 10], defaultPageSize: 5, showQuickJumper:true }}/>
                </div>

            </div>
        )
    }
}

export default PlayersPage

