# Nico Rodriguez Website Backend

A Node.js/Express backend API for the personal website of Nico Rodriguez.

## Features

- Express.js server with TypeScript
- CORS enabled for frontend integration
- Placeholder API endpoints
- Health check endpoint
- Error handling middleware

## Development

### Prerequisites

- Node.js 18+ 
- npm

### Installation

```bash
npm install
```

### Running in Development

```bash
npm run dev
```

The server will start on `http://localhost:3001`

### Building for Production

```bash
npm run build
npm start
```

## API Endpoints

### Health Check
- `GET /health` - Returns API status

### Placeholder Endpoints
- `GET /api` - Main API info
- `GET /api/status` - API status
- `GET /api/projects` - Projects data (placeholder)
- `POST /api/contact` - Contact form (placeholder)

## Environment Variables

Create a `.env` file in the root directory:

```
PORT=3001
NODE_ENV=development
```

## Future Development

This backend is currently a placeholder. Future features will include:

- Database integration
- Contact form handling
- Project data management
- Authentication system
- Blog post management
- Analytics tracking

## License

ISC
