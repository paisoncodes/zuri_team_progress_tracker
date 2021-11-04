import axiosConfig from "./axiosConfig"
import axiosClientForm from "./axiosConfig"

class ContributionServices {
    getIntern(){
        return axiosConfig.get("/api/v1/interns/?page=1")
    }
    getStackYear(year) {
        return axiosConfig.get(`/api/v1/stacks/batch/${year}/`)
    }
    getAllStack(year){
        return axiosConfig.get(`/api/v1/interns/batch/${year}/?page=1`)
    }
    getStack(stack, year){
        return axiosConfig.get(`/api/v1/interns/batch/${year}/stack/${stack}/?page=1`)
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
    editIntern(intern_id, data){
        return axiosConfig.put(`/api/v1/interns/${intern_id}/update/`, data)
    }
    postJob(intern_id,data){
        return axiosClientForm.post(`/api/v1/interns/${intern_id}/jobs/`, data)
    }
    getProgresStat() {
        return axiosConfig.get("/api/v1/statistics/")
    }
}

export default new ContributionServices();