import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getRestaurants } from '../../actions/restaurants'
import restaurants from '../../reducers/restaurants';

class Restaurants extends Component {
    static PropTypes = {
        restaurants: PropTypes.array.isRequired
    }

    componentDidMount() {
        console.log('Restaurant.js')
        this.props.getRestaurants()
    }

    render() {
        return (
            <Fragment>
                <h1>Restaurants</h1>
                <div>
                    {this.props.restaurants.map(restaurant => (
                        <div key={restaurant.id}> 
                            <div>{restaurant.name}</div>
                            <div>{restaurant.address}</div>
                            <div>{restaurant.thumb}</div>
                            <div>{restaurant.url}</div>
                            <div>{restaurant.menu_url}</div>
                            <div>{restaurant.has_table_booking}</div>
                            <div>{restaurant.has_online_delivery}</div>
                        </div>
        
                    ))}
                </div>
            </Fragment>
        );
    }
}

const mapStateToProps = state => ({
    restaurants: state.restaurants.restaurants
})

export default connect(mapStateToProps, { getRestaurants })(Restaurants);