// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        // Redirecionar a rota /normalize especificamente para o serviço no Vercel
        source: '/normalize',
        destination: process.env.NODE_ENV === 'production'
          ? 'https://service-standardization-text-api.vercel.app/normalize'
          : 'http://localhost:5005/normalize'
      },
      {
        // Redirecionar outras chamadas de API
        source: '/api/:path*',
        destination: process.env.NODE_ENV === 'production'
          ? 'https://your-vercel-deployment-url/api/:path*'
          : 'http://localhost:5005/api/:path*'
      }
    ]
  },
};
