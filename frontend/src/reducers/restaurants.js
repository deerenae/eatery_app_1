import { GET_RESTAURANTS } from '../actions/types.js';

const initialState = {
    restaurants: []
}

export default function(state = initialState, action){
    switch (action.type) {
        case GET_RESTAURANTS:
            return {
                ...state,
                restaurants: action.payload
            };
        default:
            return state;
    }
}