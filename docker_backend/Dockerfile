FROM node:20

WORKDIR /app

RUN apt-get update && apt-get install -y git

RUN rm -rf /page-one

RUN git clone https://github.com/iragca/page-one.git

WORKDIR /app/page-one

RUN npm install

# Expose port
EXPOSE 5000

# Start the app
CMD ["node", "src/server.js"]
