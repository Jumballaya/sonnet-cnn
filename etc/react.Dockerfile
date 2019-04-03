FROM node:10-stretch

RUN useradd -ms /bin/bash react_app
WORKDIR /home/react_app

ENV PATH /home/react_app/node_modules/.bin:$PATH

COPY ../frontend/package.json package.json
RUN npm install --silent
RUN npm install react-scripts -g --silent

EXPOSE 3000
CMD ["npm", "start"]
