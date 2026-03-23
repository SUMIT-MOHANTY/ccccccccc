import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<h1>Fin Insurance Sandbox Ready!</h1>} />
          <Route path="/dashboard" element={<h2>Dashboard</h2>} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
