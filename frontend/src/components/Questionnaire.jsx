import React, { useState } from 'react';

const QuestionnaireForm = ({ questionnaire, onSubmit }) => {
  const [responses, setResponses] = useState({
    mood: '',
    symptoms: [],
  });

  // Handle the form changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setResponses((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleCheckboxChange = (e) => {
    const { value, checked } = e.target;
    setResponses((prev) => {
      const symptoms = checked
        ? [...prev.symptoms, value]
        : prev.symptoms.filter((symptom) => symptom !== value);

      return { ...prev, symptoms };
    });
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(responses);  // Send the responses to the backend
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>{questionnaire.mood}</h2>
      <select
        name="mood"
        value={responses.mood}
        onChange={handleInputChange}
      >
        <option value="">Select your mood</option>
        <option value="stress">Stress</option>
        <option value="calm">Calm</option>
      </select>

      <h3>{questionnaire.symptoms}</h3>
      <div>
        <label>
          <input
            type="checkbox"
            value="focus issues"
            onChange={handleCheckboxChange}
          />
          Focus Issues
        </label>
        <label>
          <input
            type="checkbox"
            value="migraine"
            onChange={handleCheckboxChange}
          />
          Migraine
        </label>
      </div>

      <button type="submit">Submit</button>
    </form>
  );
};

export default QuestionnaireForm;
