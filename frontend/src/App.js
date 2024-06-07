import React, { useState } from 'react';

function App() {
  const [inputText, setInputText] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('http://127.0.0.1:5000/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input_text: inputText })
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div className="App">
      <h1>Ask GPT-4</h1>
      <form onSubmit={handleSubmit}>
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
