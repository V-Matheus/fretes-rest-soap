import Fastify from 'fastify'

const buildServer = () => {
  const fastify = Fastify({ logger: true })

  // Accept XML body types (text/xml, application/xml) without parsing into JS
  fastify.addContentTypeParser(['text/xml', 'application/xml'], { parseAs: 'string' }, function (req, body, done) {
    done(null, body)
  })

  // Accept any POST (SOAP envelope) and return an XML response
  fastify.post('/', async (request, reply) => {
    const xml = `<?xml version="1.0"?>
<Envelope>
  <Body>
    <GetFretesResponse>
      <Fretes>
        <Frete>
          <Servico>Economico</Servico>
          <Valor>12.5</Valor>
          <Prazo>7</Prazo>
        </Frete>
        <Frete>
          <Servico>Standard</Servico>
          <Valor>20.0</Valor>
          <Prazo>5</Prazo>
        </Frete>
      </Fretes>
    </GetFretesResponse>
  </Body>
</Envelope>`
    reply.header('Content-Type', 'text/xml; charset=utf-8')
    return reply.send(xml)
  })

  return fastify
}

if (require.main === module) {
  const server = buildServer()
  const port = Number(process.env.PORT || 8002)
  server.listen({ port, host: '0.0.0.0' }).catch(err => {
    server.log.error(err)
    process.exit(1)
  })
}

export default buildServer
