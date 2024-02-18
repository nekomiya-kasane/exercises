import axios from "axios";

export const login = async(username,password)=>{
    try{
        const res = await axios.post('http://sefdb02.qut.edu.au:3000/user/login',{
            'Content-Type': 'application/json',
            "email": username,
            "password": password,
            "longExpiry": false
            })
        return res
    } catch {
        throw new Error('LoginError');
    }

}

export const refresh = async(refreshToken)=>{
    const res = await axios.post('http://sefdb02.qut.edu.au:3000/user/refresh',{
        "refreshToken": refreshToken
        })
    return res.data
}

export const getPeopleInfo = async (id, authorization) => {

    try{
        const res = await axios.get(`http://sefdb02.qut.edu.au:3000/people/${id}`, {
            headers: {
                'Authorization': `Bearer ${authorization}`,
                'Content-Type': 'application/json',
            },
            });
            return res.data;
    } catch {
        throw new Error('GetPeopleInfoError');
    }
  };

export const register = async(username,password)=>{
    const res = await axios.post('http://sefdb02.qut.edu.au:3000/user/register',{
        'Content-Type': 'application/json',
        "email":username,
        "password":password
    })
    return res
}

export const logout = async (refreshToken) =>{
    const res = await axios.post('http://sefdb02.qut.edu.au:3000/user/logout',{
        'Content-Type': 'application/json',
        "refreshToken":refreshToken
    })
    return res
}
