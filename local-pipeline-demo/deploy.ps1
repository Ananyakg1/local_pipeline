# Local deployment script for Windows PowerShell
Write-Host "Building Docker image..."
docker build -t local-pipeline-demo .
Write-Host "Running Docker container..."
docker run --rm --name local-pipeline-demo-app local-pipeline-demo
