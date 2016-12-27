echo "Building image to your library as scroll-phat"

# Maintainers do not want Dockerfile at root of repository.
cp Dockerfile ../
cd ../
docker build -t scroll-phat . && rm Dockerfile



