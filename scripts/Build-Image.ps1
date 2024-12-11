$imageExists = docker images -q "fastapi-app"

if ($imageExists) {
    docker image rm "$imageExists"
}

docker build -t "fastapi-app" .