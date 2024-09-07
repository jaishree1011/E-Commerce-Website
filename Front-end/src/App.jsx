import { useState } from 'react'
import './App.css'
import { Route, Routes, BrowserRouter } from 'react-router-dom'
import Login from './views/auth/Login'
import Register from './views/auth/Register'
import Dashboard from './views/auth/Dashboard'
import Logout from './views/auth/Logout'
import StoreHeader from './views/base/StoreHeader'
import StoreFooter from './views/base/StoreFooter'
import Products from './views/store/Products'
import ProductDetail from './views/store/ProductDetail'

function App() {
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      <StoreHeader />
        <Routes>
          <Route path='/login' element={<Login />}/>
          <Route path='/register' element={<Register />}/>
          <Route path='/logout' element={<Logout />}/>
          <Route path='/dashboard' element={<Dashboard />}/>
          <Route path='/' element={<Products />}/>
          <Route path='/detail/:slug/' element={<ProductDetail />} />
        </Routes>
      <StoreFooter />
    </BrowserRouter>
  )
}

export default App
