### Dockerfile for using the `scrollphat` library without needing to install it on base system.

To learn how to install Docker on a Pi visit:

* [Hands-on Docker for Raspberry Pi](http://blog.alexellis.io/hands-on-docker-raspberrypi/)

For a curated collection of tutorials and images for Docker on ARM (Raspberry Pi) visit:

* https://github.com/alexellis/docker-arm

### Building:

Build the local source as a Docker image:

```
$ ./build_docker.sh
```

Or build from the master branch on Github with:

```
$ ./build_docker_git.sh
```

#### Running in a REPL

```
$ docker run -ti --privileged scroll-phat

Python 2.7.9 (default, Mar  8 2015, 00:52:26)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import scrollphat
>>> scrollphat.set_pixel(1,1,True)
>>> scrollphat.update()
>>>
```

#### Adding your own code

Build an image to run an example file:

**Dockerfile**

```
FROM scroll-phat
CMD ["python", "examples/count.py", "99"]
```

**Build example**

```
docker build -t scroll-phat/count .
```

**Running an example**

```
docker run --privileged scroll-phat/count
```

### Use-cases for Docker

#### Testing use-case

* Remove all traces of scroll-phat egg from base system
* Use Dockerfile to run `setup.py install` then run a number of the examples to see whether they are working fully.

* Can easily have an image with only Python2, only Python3 and both - for testing.

Previously this would have involved hacks and work-arounds.

#### Deployment use-case

* Once i2c is configured on the base system, nothing needs to be installed on top at all
* Everything can be installed straight into the image - even at different versions
* Can be used as a base image to be derived from for a personal project with scroll-phat

#### Can be used to distribute a tested/working installation

Maintainer builds image -> maintainer uploads to Docker Hub -> consumer/enthusiast pulls image, runs exactly the same as it did for the maintainer.

