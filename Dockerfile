FROM alpine:latest
RUN apk add --no-cache bash procps
WORKDIR /app
COPY scripts/container.sh /app/container.sh
RUN chmod +x /app/container.sh
CMD ["/app/container.sh"]
