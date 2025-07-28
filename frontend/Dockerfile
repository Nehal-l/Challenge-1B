# Build Stage
FROM node:18 as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Production Stage with Nginx
FROM nginx:alpine

# Copy built React app to nginx
COPY --from=build /app/build /usr/share/nginx/html

# Copy custom nginx config to support client-side routing (optional)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
