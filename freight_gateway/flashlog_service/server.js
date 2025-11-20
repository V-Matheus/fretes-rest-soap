const fastify = require('fastify')({ logger: true })

fastify.get('/fretes', async (request, reply) => {
  const cep = request.query.cep || ''
  // Simula opções caras e rápidas
  const resp = {
    options: [
      { service: 'Express', price: 49.9, eta_days: 1 },
      { service: 'Normal', price: 30.0, eta_days: 3 }
    ]
  }
  return resp
})

const start = async () => {
  try {
    const port = process.env.PORT || 8001
    await fastify.listen({ port: Number(port), host: '0.0.0.0' })
  } catch (err) {
    fastify.log.error(err)
    process.exit(1)
  }
}
start()
