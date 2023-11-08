# build
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run lint --fix \
    && npm run build

# prod
FROM nginx:stable-alpine as production-stage
VOLUME /var/log/nginx
# COPY nginx-main.conf /etc/nginx/nginx.conf
# COPY nginx-server.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/dist /usr/share/nginx/html
# RUN apk --no-cache add dos2unix \
#     && dos2unix /etc/nginx/conf.d/default.conf \
#     && find /usr/share/nginx/html -type f -exec dos2unix {} +
EXPOSE 80
CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]