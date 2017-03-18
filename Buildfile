git add *.py
git add Dockerfile
git add Buildfile
git commit -m "From Buildfile"
git push
docker rmi tfrecommgpu
docker build -t tfrecommgpu .
docker tag tfrecommgpu acobley/tfrecommgpu
docker push acobley/tfrecommgpu
docker rm runtfrecommgpu
docker run --name runtfrecommgpu -p 81:81 -i -t acobley/tfrecommgpu bash
