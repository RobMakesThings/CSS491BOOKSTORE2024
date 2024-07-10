export default class AuthService {

    
    login(username,password) {

        let form = new FormData()
        form.append("grant_type:","password")
        form.append("username",`${username}`)
        form.append("password",`${password}`)


        return fetch('api/token/',
        {
            method:"POST",
            body:form

            
            
        })
            .then((res) => res.json())
            .then((d) => d.data);
    }
}