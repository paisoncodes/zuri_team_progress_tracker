import Axios from 'axios';

const axiosClient = Axios.create({
    baseURL: 'https://zuri-progress-tracker.herokuapp.com/',
    withCredentials: false,
    headers: {
        // Accept: 'application/json',
        // 'Content-Type': 'application/json',
        'Content-Type': 'multipart/form-data'
    },
});

// const axiosClientForm = Axios.create({
//     baseURL: 'https://zuri-progress-tracker.herokuapp.com/',
//     withCredentials: false,
//     headers: {
//         'Content-Type': 'multipart/form-data'
//     },
// });

export default axiosClient