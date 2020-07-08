import axios from 'axios';
import { GET_RESTAURANTS } from './types';


export const getRestaurants = () {
    fetch('localhost:8000/api/restaurants/')
    .then(response => response.json())
    .then(restaurants => console.log(restaurants, "rests"))

}