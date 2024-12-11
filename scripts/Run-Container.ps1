param (
    [Parameter(Mandatory, HelpMessage="Enter the folder containing your src folder.")]
    [ValidateScript({-not [string]::IsNullOrWhitespace($_)})]
    [string]$appFolder
)

$containerName = "$appFolder"
$networkName = "db-network"

$containerExists = docker ps -a -q -f name=$containerName

if (-not $containerExists) {
    Write-Host "No container $containerName found, executing docker run"

    $networkExists = docker network ls -q -f name=$networkName

    Write-Host "network $networkExists"

    if(-not $networkExists) {
        docker network create -d bridge $networkName
    }

    docker run -d `
    -p 8000:8000 `
    --mount type=bind,source="$(Get-Location)/$appFolder/src",target="/app/src" `
    --rm `
    --network="$networkName" `
    --name $containerName `
    "fastapi-app"
} else {
    $containerRunning = docker ps -q -f "status=running" -f "name=$containerName"
    
    if ($containerRunning) {
        Write-Host "The container $containerName is already running"
    }
}