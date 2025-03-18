# Use an official Node.js runtime as the base image
ARG NODE_VERSION=14.17.5
FROM node:${NODE_VERSION}-alpine as base

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json first (to leverage Docker caching)
COPY package.json package-lock.json ./

# Install dependencies (including dev dependencies for development)
RUN npm install

# Copy the rest of the application files
COPY . .

# Ensure node_modules stays in the image
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# Expose the app port
EXPOSE 3000

# Set environment
ENV NODE_ENV development

# Start the application
CMD ["npm", "start"]
