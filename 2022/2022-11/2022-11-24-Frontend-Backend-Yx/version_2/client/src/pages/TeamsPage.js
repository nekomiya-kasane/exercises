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
import { getTeamWinLoseMost } from '../fetcher'
const wideFormat = format('.3r');
// const bodyParser = require("body-parser"); router.use(bodyParser.json());

const winLoseMostColumns = [
    {
        title: 'Season',
        dataIndex: 'SEASON',
        key: 'SEASON',
        sorter: (a, b) => a.SEASON.localeCompare(b.SEASON),
    },
    {
        title: 'Opponent ID',
        dataIndex: 'OPPONENT_ID',
        key: 'OPPONENT_ID',
        sorter: (a, b) => a.OPPONENT_ID.localeCompare(b.OPPONENT_ID)
    },
    {
        title: '# Wins',
        dataIndex: 'N_WINS',
        key: 'N_WINS',
        sorter: (a, b) => a.N_WINS - b.N_WINS

    },
    {
        title: '# Losses',
        dataIndex: 'N_LOSSES',
        key: 'N_LOSSES',
        sorter: (a, b) => a.N_LOSSES - b.N_LOSSES

    },

];


class TeamsPage extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            teamIDQuery:'',
            // teamsResults: [],
            winLoseMostResults: []
        }

        this.handleTeamIDQueryChange = this.handleTeamIDQueryChange.bind(this)
        this.updateSearchResults = this.updateSearchResults.bind(this)
    }

    handleTeamIDQueryChange(event) {
        this.setState({ teamIDQuery: event.target.value })
    }

    updateSearchResults() {
        getTeamWinLoseMost(this.state.teamIDQuery).then(res => {
            this.setState({ winLoseMostResults: res.results })
        })
    }

    // componentDidMount() {
    //     if (this.state.teamIDQuery > 0) {
    //         getPlayer(this.state.teamIDQuery).then(res => {
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
                            <label>Team ID</label>
                            <FormInput placeholder="Team ID" value={this.state.teamIDQuery} onChange={this.handleTeamIDQueryChange} />
                        </FormGroup></Col>

                        <Col flex={2}><FormGroup style={{ width: '10vw' }}>
                            <Button style={{ marginTop: '4vh' }} onClick={this.updateSearchResults}>Search</Button>
                        </FormGroup></Col>
                    </Row>
                    <br></br>
                </Form>

                <Divider />

                <div style={{ width: '70vw', margin: '0 auto', marginTop: '2vh' }}>
                <Table dataSource={this.state.winLoseMostResults} columns={winLoseMostColumns} pagination={{ pageSizeOptions:[5, 10], defaultPageSize: 5, showQuickJumper:true }}/>
                </div>

                {/* <Divider />

                <Row>
                    <Col flex={2}><FormGroup style={{ width: '20vw', margin: '0 auto' }}>
                        <label>Player A</label>
                        <FormInput placeholder="Player A ID" value={this.state.teamAIDQuery} onChange={this.handlePlayerAIDQueryChange} />
                    </FormGroup></Col>

                    <Col flex={2}><FormGroup style={{ width: '20vw', margin: '0 auto' }}>
                        <label>Player B</label>
                        <FormInput placeholder="Player B ID" value={this.state.teamBIDQuery} onChange={this.handlePlayerBIDQueryChange} />
                    </FormGroup></Col>

                    <Col flex={2}><FormGroup style={{ width: '10vw' }}>
                        <Button style={{ marginTop: '4vh' }} onClick={this.updateCompareResults}>Compare</Button>
                    </FormGroup></Col>
                </Row>

                <div style={{ width: '70vw', margin: '0 auto', marginTop: '2vh' }}>
                <Table dataSource={this.state.winLoseMostResults} columns={winLoseMostColumns} pagination={{ pageSizeOptions:[5, 10], defaultPageSize: 5, showQuickJumper:true }}/>
                </div> */}

            </div>
        )
    }
}

export default TeamsPage

