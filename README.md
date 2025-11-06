# Canvas Dump API

Minimal deployment package for the Canvas course dump API.

## Deploy to Railway

1. Initialize git:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Create GitHub repo at https://github.com/new

3. Push code:
   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/canvas-api.git
   git branch -M main
   git push -u origin main
   ```

4. Deploy on Railway:
   - Go to railway.app
   - Click "Deploy from GitHub repo"
   - Select your new repo
   - Add environment variables:
     - `CANVAS_TOKEN` (your Canvas API token)
     - `SUBJECTFOCUS_API_KEY` (your secret key)

## Environment Variables

- `CANVAS_TOKEN` - Your Canvas LMS API token (required)
- `SUBJECTFOCUS_API_KEY` - API key for authentication (optional but recommended)

## Endpoints

- `GET /health` - Health check
- `GET /dump?course_id=X` - Dump course (blocking)
- `GET /dump/async?course_id=X` - Dump course (async, recommended)
- `GET /status/{job_id}` - Check job status
- `GET /jobs` - List all jobs

Full docs at: `/docs`
