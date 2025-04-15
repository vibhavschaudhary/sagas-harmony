import React, { useState } from 'react';

const QuestionnaireForm = ({ questionnaire, onSubmit }) => {
  const [responses, setResponses] = useState({});

  // Handle the form changes for single-select and multiple-select questions
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setResponses((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleCheckboxChange = (e) => {
    const { name, value, checked } = e.target;
    setResponses((prev) => {
      const updatedValue = checked
        ? [...(prev[name] || []), value]  // Add value to array if checked
        : prev[name].filter((item) => item !== value); // Remove value if unchecked

      return { ...prev, [name]: updatedValue };
    });
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(responses);  // Send responses to backend
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>{questionnaire.title}</h2>

      {questionnaire.questions.map((question) => (
        <div key={question.id}>
          <h3>{question.text}</h3>

          {/* Single-choice questions */}
          {question.type === 'single' && (
            <select
              name={question.id}
              value={responses[question.id] || ''}
              onChange={handleInputChange}
            >
              <option value="">Select your answer</option>
              {question.options.map((option, index) => (
                <option key={index} value={option}>
                  {option}
                </option>
              ))}
            </select>
          )}

          {/* Multiple-choice questions */}
          {question.type === 'multiple' && (
            <div>
              {question.options.map((option, index) => (
                <label key={index}>
                  <input
                    type="checkbox"
                    name={question.id}
                    value={option}
                    onChange={handleCheckboxChange}
                  />
                  {option}
                </label>
              ))}
            </div>
          )}
        </div>
      ))}

      <button type="submit">Submit</button>
    </form>
  );
};

export default QuestionnaireForm;
