# Use an official lightweight Node.js image
FROM node:20-alpine

# Set the working directory inside the container
WORKDIR /app

COPY package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of the frontend source code
COPY . .

# Inform Docker that the container listens on Vite's default port
EXPOSE 5173

# Run the dev server and bind to all network interfaces
CMD ["npm","run","dev","--","--host"]