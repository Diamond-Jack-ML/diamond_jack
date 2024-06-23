import React, { useState } from 'react';

function App() {
  const [inputText, setInputText] = useState('');
  const [userRole, setUserRole] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://127.0.0.1:5000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input_text: inputText, user_role: userRole })
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className="App">
      <h1>Main System</h1>
      <form onSubmit={handleSubmit}>
      <label>
          Enter your role:
          <input
            type="text"
            value={userRole}
            onChange={(e) => setUserRole(e.target.value)}
          />
        </label>
        <br />
        <label>
          Enter your text:
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            rows="4"
            cols="50"
          />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
      <h2>Response:</h2>
      <p>{response}</p>
    </div>
  );
}

export default App;
