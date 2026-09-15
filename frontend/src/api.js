const API_BASE_URL = 'http://localhost:8000/api';

export const scanImage = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch(`${API_BASE_URL}/scan`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error scanning image:', error);
    throw error;
  }
};

export const fetchInsights = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/insights`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error fetching insights:', error);
    throw error;
  }
};
