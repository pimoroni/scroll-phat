echo "Building image to your library as scroll-phat"
cp Dockerfile ../
cd ../
docker build -t scroll-phat .
rm Dockerfile


