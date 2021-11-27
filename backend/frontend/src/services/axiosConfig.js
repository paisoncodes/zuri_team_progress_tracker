import Axios from 'axios';

const axiosClient = Axios.create({
    baseURL: 'https://progress.zuri.team/',
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
    },
});

export const axiosClientForm = Axios.create({
    baseURL: 'https://progress.zuri.team/',
    withCredentials: false,
    headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'multipart/form-data'
    },
});

export default axiosClient