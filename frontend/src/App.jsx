import React, { useState } from 'react';
import axios from 'axios';
import SummaryCard from './components/SummaryCard';

function App() {
  const [note, setNote] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSummarize = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await axios.post('http://localhost:8000/notes/', { content: note });
      setSummary(response.data.summary);
    } catch (err) {
      setError('Failed to fetch summary. Please try again.');
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-4">
      <h1 className="text-3xl font-bold mb-6 text-center">📝 AI Notes Summarizer</h1>
      <textarea
        value={note}
        onChange={(e) => setNote(e.target.value)}
        placeholder="Enter your note here..."
        rows="10"
        className="w-full max-w-2xl p-4 rounded-lg border shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 mb-4"
      />
      <button
        onClick={handleSummarize}
        disabled={loading || !note.trim()}
        className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 disabled:bg-blue-300 transition"
      >
        {loading ? 'Summarizing...' : 'Summarize'}
      </button>

      {error && <p className="text-red-500 mt-4">{error}</p>}

      {summary && !error && (
        <SummaryCard summary={summary} />
      )}
    </div>
  );
}

export default App;
