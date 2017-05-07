git add *.py
git add Dockerfile
git add Buildfile
git add download_data.sh
git commit -m "From Buildfile ml-latest-small"
git push
docker rmi tfrecommgpu-small
docker build -t tfrecommgpu-small .
docker tag tfrecommgpu-small acobley/tfrecommgpu-small
docker push acobley/tfrecommgpu-small
docker rm runtfrecommgpu-small
docker run --name runtfrecommgpu-small -p 81:81 -i -t acobley/tfrecommgpu-small bash
