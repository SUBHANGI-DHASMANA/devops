### 1. Flask JSON API

A simple Flask application that exposes an `/api` endpoint to return data from a backend JSON file.

The API reads data from a local `data.json` file and sends it as a JSON response.


### 2. Flask Form Submission with MongoDB Atlas

Application Flow

1. User fills the form on the frontend
2. Frontend sends a POST request to the backend `/submit` endpoint
3. Backend inserts data into MongoDB Atlas
4. Backend returns:
   - **200 OK** on success
   - **4xx / 5xx** on error
5. Frontend:
   - Redirects to success page if response is successful
   - Displays error message on the same page if submission fails


Backend Implementation

- Receive JSON data
- Insert data into MongoDB Atlas
- Return proper HTTP status codes and JSON responses
- Handle errors gracefully

Example Response
**Success**
```json
{
  "message": "Data submitted successfully"
}
