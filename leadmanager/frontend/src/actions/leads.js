import axios from 'axios';
import {GET_LEADS} from './types'

// GET Leads
export const getLeads = () => dispatch => {
    axios.get('/api/leads/')
    .then(res =>{
        dispatch({
            types: GET_LEADS,
            payload: res.data
        })
    }).catch(err => console.log(err))
}