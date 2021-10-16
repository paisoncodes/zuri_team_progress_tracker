import axiosConfig from "./axiosConfig"

class ContributionServices {
    // exampleFunc(){
    //     return axiosConfig.get('/sample')
    // }
    getTotalSalary() {
        return axiosConfig.get("/interns/total_salary")
    }
}

export default new ContributionServices();