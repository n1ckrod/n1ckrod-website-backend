import express from 'express';

const router = express.Router();

// Placeholder API endpoints
router.get('/', (req, res) => {
  res.json({ 
    message: 'API under development',
    status: 'placeholder',
    endpoints: [
      'GET /api - This endpoint',
      'GET /api/status - API status',
      'GET /api/projects - Projects data (placeholder)',
      'GET /api/contact - Contact form (placeholder)'
    ]
  });
});

router.get('/status', (req, res) => {
  res.json({ 
    status: 'operational',
    message: 'API under development',
    timestamp: new Date().toISOString(),
    version: '1.0.0'
  });
});

router.get('/projects', (req, res) => {
  res.json({ 
    message: 'API under development',
    data: [],
    note: 'This endpoint will return project data in the future'
  });
});

router.post('/contact', (req, res) => {
  res.json({ 
    message: 'API under development',
    status: 'placeholder',
    note: 'Contact form submission will be implemented in the future'
  });
});

export default router;
