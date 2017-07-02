git add *.py
git add Dockerfile
git add Buildfile
git commit -m "From Buildfile"
git push
docker rmi tfrecommgpum
docker build -t tfrecommgpum .
docker tag tfrecommgpum acobley/tfrecommgpum
docker push acobley/tfrecommgpum
docker rm runtfrecommgpum
docker run --name runtfrecommgpum -p 81:81 -i -t acobley/tfrecommgpum bash
