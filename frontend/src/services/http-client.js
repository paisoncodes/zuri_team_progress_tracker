import axiosConfig from "./axiosConfig"

class ContributionServices {
    exampleFunc(){
        return axiosConfig.get('/sample')
    }
    getIntern(){
        return axiosConfig.get("/api/v1/interns/")
    }
    getStack(stack){
        return axiosConfig.get(`/api/v1/interns/stack/${stack}/`)
    }
    getTotalSalary() {
        return axiosConfig.get("/api/v1/interns/total_salary")
    }
    getStatistics(year) {
        return axiosConfig.get(`/api/v1/statistics/batch/${ year }`)
    }
    getJobs(user_id) {
        return axiosConfig.get(`/api/v1/interns/${user_id}/jobs/`)
    }
}

export default new ContributionServices();