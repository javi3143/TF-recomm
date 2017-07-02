git add *.py
git add Dockerfile
git add Buildfile
git commit -m "From Buildfile"
git push
docker rmi tfrecommgpuM
docker build -t tfrecommgpuM .
docker tag tfrecommgpuM acobley/tfrecommgpuM
docker push acobley/tfrecommgpuM
docker rm runtfrecommgpuM
docker run --name runtfrecommgpuM -p 81:81 -i -t acobley/tfrecommgpuM bash
