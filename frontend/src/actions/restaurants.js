import axios from 'axios';
import { GET_RESTAURANTS } from './types';
import { YELP_API_KEY } from './.env';

export const getRestaurants = () => dispatch => {
    fetch('https://api.yelp.com/v3/businesses/search?term=restaurants&location=denver/',
    {
        method: 'GET',
        headers: {'Authorization': `Bearer ${YELP_API_KEY}`, 'Access-Control-Allow-Origin': '*'}

    }
    ).then(response => response.json())
    .then(restaurants => console.log(restaurants, "rests"))

}