import Axios from 'axios';

const axiosClient = Axios.create({
    baseURL: 'https://zuri-progress-tracker.herokuapp.com/',
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
    },
});

export default new axiosClient