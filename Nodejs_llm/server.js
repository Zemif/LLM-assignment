const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const port = 3000;

app.use(express.json());

app.post('/query', async (req, res) => {
  try {
    const { model, query } = req.body;
    const response = await axios.post('http://python_llm:5000/query', { model, query });
    res.json(response.data);
  } catch (error) {
    console.log(error.response);
    console.error('Error sending query:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.listen(port, () => {
  console.log(`Node.js app listening at http://localhost:${port}`);
});
