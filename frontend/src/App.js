import React, { useState, useEffect } from 'react';
import QuestionnaireForm from './components/Questionnaire';

function App() {
  const [questionnaire, setQuestionnaire] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  // Fetch questionnaire data when the component mounts
  useEffect(() => {
    fetch('http://localhost:5000/questionnaire')  // Ensure this is your backend URL
      .then((response) => response.json())
      .then((data) => {
        setQuestionnaire(data);
        setIsLoading(false);
      })
      .catch((error) => console.error('Error fetching questionnaire:', error));
  }, []);

  // Handle the form submission
  const handleSubmit = async (responses) => {
    const response = await fetch('http://localhost:5000/recommend', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ responses }),  // Send responses to backend
    });

    if (response.ok) {
      const data = await response.json();
      setRecommendations(data.recommendations);  // Set the recommendations state
    } else {
      console.error('Error:', response.statusText);
    }
  };

  return (
    <div>
      <h1>Saga's Harmony</h1>
      {isLoading ? (
        <p>Loading Questionnaire...</p>
      ) : (
        <QuestionnaireForm
          questionnaire={questionnaire}
          onSubmit={handleSubmit}  // Pass the form submission handler
        />
      )}

      <div>
        {recommendations.length > 0 && (
          <div>
            <h2>Recommendations</h2>
            <ul>
              {recommendations.map((rec, index) => (
                <li key={index}>{rec}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
