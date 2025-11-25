import Fastify from 'fastify'
import { FastifyInstance } from 'fastify'

interface Option {
  service: string
  price: number
  eta_days: number
}

const buildServer = (): FastifyInstance => {
  const fastify = Fastify({ logger: true })

  fastify.get('/fretes', async (request, reply) => {
    const cep = (request.query as any).cep || ''
    const resp = {
      options: [
        { service: 'Express', price: 49.9, eta_days: 1 },
        { service: 'Normal', price: 30.0, eta_days: 3 }
      ] as Option[]
    }
    return resp
  })

  return fastify
}

if (require.main === module) {
  const server = buildServer()
  const port = Number(process.env.PORT || 8001)
  server.listen({ port, host: '0.0.0.0' }).catch(err => {
    server.log.error(err)
    process.exit(1)
  })
}

export default buildServer
