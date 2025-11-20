FROM node:18 AS builder
WORKDIR /app

# install deps and build
COPY package.json tsconfig.json ./
COPY src ./src
RUN npm install && npm run build

FROM node:18-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package.json ./package.json
ENV NODE_ENV=production
RUN npm install --production --omit=dev

EXPOSE 8001
CMD ["node", "dist/server.js"]
