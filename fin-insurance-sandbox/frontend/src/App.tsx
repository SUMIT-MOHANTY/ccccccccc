import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import PolicyList from './pages/PolicyList'
import './App.css'

function App() {
  return (
    <div className="App">
      <header>
        <h1>Fin Insurance Sandbox</h1>
      </header>
      <main>
        <Router>
          <Routes>
            <Route path="/" element={<PolicyList />} />
          </Routes>
        </Router>
      </main>
    </div>
  )
}

export default App
