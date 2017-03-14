git add *.py
git commit -m "Buildfile"
git push
docker rmi tfrecomm
docker build -t tfrecomm .
docker tag tfrecomm acobley/tfrecomm
docker push acobley/tfrecomm
docker rm runtfrecomm
docker run --name runtfrecomm -i -t acobley/tfrecomm bash