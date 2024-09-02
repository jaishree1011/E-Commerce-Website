import React from 'react'
import { useEffect, useState } from 'react';
import { Link, useSearchParams, useNavigate } from 'react-router-dom';
import apiInstance from '../../utils/axios';


function CreatePassword() {
    const [password, setPassword] = useState("")
    const [confirmPassword, setConfirmPassword] = useState("")
    const [error, setError] = useState(null)

    const navigate = useNavigate()

    const [searchParams] = useSearchParams();
    const otp = searchParams.get('otp');
    const uidb64 = searchParams.get('uidb64');
    const reset_token = searchParams.get('reset_token');
    

    const handlePasswordSubmit = async (e) => {
        e.preventDefault()

        if (password !== confirmPassword) {
            setError(true);
            console.log("Password Does Not Match")
        } else {
            setError(false);

            console.log("otp ======", otp);
            console.log("uidb64 ======", uidb64);
            console.log("reset_token ======", reset_token);
            console.log("password ======", password);

            const formdata = new FormData()
            formdata.append("otp", otp)
            formdata.append("uidb64", uidb64)
            formdata.append("reset_token", reset_token)
            formdata.append("password", password)

            try {
                await apiInstance.post(`user/password-change/`, formdata).then((res) => {
                    console.log(res.data.code)
                    alert("Password Changed Successfully")
                    navigate("/login")
                })
            } catch (error) {
                alert("An error occured while trying to change the password")
            }
        }

    }
  return (
    <div>
        <h1>Create New Password</h1>
        <form onSubmit={handlePasswordSubmit}>
            <input
                type='password'
                name=""
                id=""
                placeholder='Enter New Password'
                onChange={(e) => setPassword(e.target.value)}
            />
            <br />
            <br />
            <input 
                type='password'
                name=''
                id=''
                placeholder='Confirm New Password'
                onChange={(e) => setConfirmPassword(e.target.value)}
            />      
        </form>
        <br/>
        <button type='submit'>Save New Password</button>

    </div>
  )
}

export default CreatePassword
