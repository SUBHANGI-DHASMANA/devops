const express = require('express');
const path = require('path');

const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.render('form', { error: null });
});

app.post('/submit', (req, res) => {
    const { name, email, password } = req.body;

    if (!name || !email || !password) {
        return res.render('form', {
            error: 'All fields are required'
        });
    }

    console.log({ name, email, password });

    res.send('Form submitted successfully');
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server listening on http://localhost:${PORT}`);
});
