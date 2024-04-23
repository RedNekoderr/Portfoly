# Specify the base image
FROM node:lts-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json ./
COPY yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the code
COPY . .

# Build the SvelteKit app
RUN yarn build

# Expose the necessary port
EXPOSE 3000

# Specify the command to run the app
CMD ["yarn", "run", "preview", "--port", "3000", "--host", "0.0.0.0"]
