import React from 'react';

const SummaryCard = ({ summary }) => {
  return (
    <div className="mt-6 w-full max-w-2xl bg-white p-6 rounded-xl shadow-lg">
      <h2 className="text-xl font-semibold mb-2">🔍 Summary</h2>
      <p className="text-gray-700">{summary}</p>
    </div>
  );
};

export default SummaryCard;
