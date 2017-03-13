docker build -t tfrecomm .
docker tag tfrecomm acobley/tfrecomm
docker push acobley/tfrecomm
docker rm tfrecomm
docker run --name tfrecomm -i -t acobley/tfrecomm bash