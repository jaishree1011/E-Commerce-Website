import { useState} from 'react'
import apiInstance from '../../utils/axios'
import { useSearchParams } from 'react-router-dom';
import { useNavigate } from 'react-router-dom'

function ForgotPassword() {
    const [email, setEmail] = useState("")

    const [searchParams] = useSearchParams();
    const otp = searchParams.get('otp');
    const uuid = searchParams.get('uuid');

    const navigate = useNavigate()

    const handleSubmit =async() => {
        try{
        await apiInstance.get(`user/password-reset/${email}/`).then((res) =>{
            alert("An Email Has Been Sent to you")
            navigate("/create-new-password")        
        })
    }catch(error){
        alert("Email Does Not Exists")
    }
    }

  return (
    <div>
        <h1>Forgot Password</h1>
        <input onChange={(e) => setEmail(e.target.value)}
            type='email' 
            placeholder='Enter Email' 
            name="" 
            id=''
        />
        <br />
        <br />
        <button onClick={handleSubmit}>Reset Password</button>
    </div>
  )
}

export default ForgotPassword
