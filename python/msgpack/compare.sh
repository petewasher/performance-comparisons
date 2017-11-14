docker build . -f Dockerfile -t python-msgpack-comparison
docker build . -f Dockerfile-pypy -t pypy-msgpack-comparison

echo "Running in python..."
docker run --rm python-msgpack-comparison

echo "Running in pypy..."
docker run --rm pypy-msgpack-comparison