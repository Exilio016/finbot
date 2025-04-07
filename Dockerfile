FROM alpine:3.21 
COPY uv.lock uv.lock
COPY pyproject.toml pyproject.toml
COPY src src
COPY generated generated
RUN apk update && apk upgrade && apk add uv && apk add python3
CMD ["uv", "run", "-m", "src"]
