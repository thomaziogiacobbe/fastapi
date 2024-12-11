$networkName = "db-network"

$networkExists = docker network ls -q -f name=$networkName

if(-not $networkExists) {
    docker network create -d bridge $networkName
}