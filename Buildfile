git add *.py
git add Dockerfile
git add Buildfile
git commit -m "From Buildfile"
git push
docker rmi tfrecomm-ml-latest-small
docker build -t tfrecomm-ml-latest-small .
docker tag tfrecomm-ml-latest-small acobley/tfrecomm-ml-latest-small
docker push acobley/tfrecomm-ml-latest-small
docker rm runtfrecomm-ml-latest-small
docker run --name runtfrecomm-ml-latest-small -p 81:81 -i -t acobley/tfrecomm-ml-latest-small bash