const express = require('express');
const path = require('path');

const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.render('form', { error: null });
});

const axios = require('axios');

app.post('/submit', async (req, res) => {
    const { name, email, password } = req.body;

    if (!name || !email || !password) {
        return res.render('form', {
            error: 'All fields are required'
        });
    }

    try {
        const response = await axios.post('http://backend:8000/submit', {
            name,
            email,
            password
        });

        res.send('Form submitted successfully to backend');
    } catch (error) {
        console.error(error.message);
        res.render('form', { error: 'Backend error' });
    }
});

app.get('/users', async (req, res) => {
    try {
        const response = await axios.get('http://backend:8000/users');
        res.render('users', { users: response.data });
    } catch (error) {
        res.status(500).send('Error fetching users');
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server listening on http://localhost:${PORT}`);
});