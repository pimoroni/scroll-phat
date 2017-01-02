echo "Building image to your library as scroll-phat:master"

# Maintainers do not want Dockerfile at root of repository.
cp git.Dockerfile ../Dockerfile
cd ../
docker build -t scroll-phat:master . && rm Dockerfile
