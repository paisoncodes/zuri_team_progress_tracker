import axiosConfig from "./axiosConfig"

class ContributionServices {
    exampleFunc(){
        return axiosConfig.get('/sample')
    }
}

export default new ContributionServices();