import React, { useEffect, useRef, useState } from 'react';
import { getSearchMovie } from '../api/movieAPI';
import { Input, Typography, Button,Form, message} from 'antd';
import { Link } from 'react-router-dom';

import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-balham.css';

import { InfiniteRowModelModule } from '@ag-grid-community/infinite-row-model';
import { ModuleRegistry } from '@ag-grid-community/core';
// Register the required feature modules with the Grid
ModuleRegistry.registerModules([InfiniteRowModelModule]);

function Movies() {
  const [name,setName] = useState('')
  const [year,setYear] = useState('')
  const [loadings, setLoadings] = useState(true);
  const [gridApi,setGridApi] = useState(null)
  const gridRef = useRef(null);
  let pageNumber = 1
  const column = [
    {
      headerName: 'Title',
      field: 'title',
      cellRenderer: function (params) {
        if(params.data) {
          return <Link to={`/moviePage/${params.data.imdbID}`}>{params.data.title}</Link>  
        }
        return null
      }
    },
    {
      headerName: 'Year',
      field: 'year',
    },
    {
      headerName: 'IMDB Rating',
      field: 'imdbRating',
    },
    {
      headerName: 'Rotten Tomatoes Rating',
      field: 'rottenTomatoesRating',
    },
    {
      headerName: 'Metacritic',
      field: 'metacriticRating',
    },
    {
      headerName: 'Rated',
      field: 'classification',
    },
  ]
  useEffect(()=>{
    setLoadings(true)
  },[])
  useEffect(()=>{
    if(gridRef.current.api) {
      if(loadings) {
        gridRef.current.api.showLoadingOverlay();
      } else {
        gridRef.current.api.hideOverlay();
      }
    }
  },[loadings])
  const onFinish=async()=>{
    pageNumber = 1
    setLoadings(true)
    onGridReady(gridApi)
  }

  const onGridReady= (params)=>{
      if(params){
        setGridApi(params)
      }
      const dataSource = {
        rowCount: undefined,
        getRows: (params) => {
          const requestPage = pageNumber
          getSearchMovie(name,year,requestPage).then(res=>{
            const rowsThisPage = res.data
            const lastRow = res.pagination.total
            pageNumber = res.pagination.nextPage
            params.successCallback(rowsThisPage,lastRow);
            setLoadings(false)
          }).catch(_e => {
            message.error("Unable to search, please check the conodition again!")
            setLoadings(false)
        });
        }
      }
      params.api.setDatasource(dataSource);
    }
  return (
    <div>
      <div style={{display:'flex',flexDirection:'column',alignItems:'center'}}>
        <Typography.Title >Search Your Favorite Movie</Typography.Title>
        <div>
          <Form
            name="searchForm"
            autoComplete="off"
            style={{display:'flex',flexDirection:'row',alignItems:'center'}}
            onFinish={async()=>{
              setLoadings(true)
              await onFinish()
            }}
          >
            <Form.Item
              style={{width:'500px'}}
              label="Movie Name"
              name="Move Name"
            >
              <Input 
                allowClear
                value ={name}
                style={{width:'400px'}}
                placeholder="Movie Name" 
                onChange={(e) => {
                  setName(e.target.value);
                }}/>
            </Form.Item>
            <Form.Item
              style={{width:'400px',paddingLeft:'10px',paddingRight:'10px'}}
              label="Year"
              name="Year"
              rules={[{ 
                message: "It must be number value",
                pattern: new RegExp(/^[0-9]+$/),
              }]}
            >
              <Input 
                onChange={(e) => {
                  setYear(e.target.value);
                }}/>
            </Form.Item>
            <Form.Item>
              <Button loading={loadings} type="primary" htmlType="submit">
                Search
              </Button>
            </Form.Item>
          </Form>
        </div>
      </div>
      <div style={{display:'flex',flexDirection:'column',alignItems:'center'}}>
        <div
          className="ag-theme-balham"
          style={{ height: '500px', width: '80%' }}
        >
        <AgGridReact
          ref={gridRef}
          loading={loadings}
          onGridReady={onGridReady}
          columnDefs={column}
          rowBuffer={0}
          rowSelection={'multiple'}
          rowModelType={'infinite'}
          cacheBlockSize={100}
          cacheOverflowSize={2}
          maxConcurrentDatasourceRequests={1}
          infiniteInitialRowCount={1000}
          maxBlocksInCache={10}
          overlayLoadingTemplate={'<span class="ag-overlay-loading-center">Please wait...</span>'}
        />
      </div>
      </div>
    </div>
  );
}

export default Movies;