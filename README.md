# MovieDash
🎬 A modern movie streaming platform featuring adaptive video delivery, user profiles, and personalized recommendations. Developed using React, Node.js, and a microservices architecture.

# 🎬 MovieDash

A modern, scalable movie streaming platform built with microservices architecture.

## ✨ Features

- 🎥 **Adaptive Video Streaming** - HLS/DASH with multiple quality levels (360p to 4K)
- 👥 **User Profiles** - Multiple profiles per account (Kids/Adult)
- 📺 **Watch History** - Continue watching from where you left off
-  **Personalized Recommendations** - AI-powered movie suggestions
- 🔐 **Secure Content Delivery** - Signed URLs and DRM protection
-  **Subscription Management** - Multiple plans (Basic, Standard, Premium)
-  **Responsive Design** - Works on desktop, tablet, and mobile

## ️ Architecture

### High-Level Design
- **Frontend**: React.js + Next.js with TypeScript
- **Backend**: Node.js (NestJS) microservices
- **Databases**: 
  - PostgreSQL (users, subscriptions, transactions)
  - MongoDB (movie metadata, catalogs)
  - Redis (caching, sessions)
  - Elasticsearch (full-text search)
- **Video Processing**: FFmpeg + AWS MediaConvert
- **Storage & CDN**: AWS S3 + CloudFront
- **Message Queue**: Apache Kafka/RabbitMQ

### Microservices
- User Service - Authentication & profiles
- Catalog Service - Movie metadata management
- Search Service - Elasticsearch-powered search
- Media Service - Video streaming & delivery
- Watch History Service - Progress tracking
- Recommendation Service - Personalized suggestions
- Subscription Service - Payments & plans

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL 15+
- MongoDB 6+
- Redis 7+

### Installation

```bash
# Clone the repository
git clone https://github.com/Regulus7/MovieDash.git
cd MovieDash

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env

# Run with Docker Compose
docker-compose up -d

# Start development server
npm run dev
