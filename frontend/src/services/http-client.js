import axiosConfig from "./axiosConfig"

class ContributionServices {
    exampleFunc(){
        return axiosConfig.get('/sample')
    }
    getIntern(){
        return axiosConfig.get("/api/v1/interns/")
    }
    getStackYear(year) {
        return axiosConfig.get(`/api/v1/interns/stacks/${year}/`)
    }
    getStack(stack){
        return axiosConfig.get(`/api/v1/interns/stack/${stack}/`)
    }
    getTotalSalary() {
        return axiosConfig.get("/api/v1/interns/total_salary")
    }
}

export default new ContributionServices();