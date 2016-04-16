Fully tested Dockerfile for using scroll-phat library without needing to install it on base system.

> This is unobtrusively squirrelled away in the library folder for those who are curious and interested in learning about Docker and the PI. Tested with the count.py example.

Building
```
$ cd library
$ ./docker_build.sh
```

Running in repl
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

Build an image to run an example file:

**Dockerfile**

```
FROM scroll-phat
CMD ["python", "example/count.py", "99"]
```

**Build example**
```
docker build -t scroll-phat/count .
```

**Running example**
```
docker run scroll-phat/count
```

### Testing use-case

* Remove all traces of scroll-phat egg from base system
* Use Dockerfile to run `setup.py install` then run a number of the examples to see whether they are working fully.

* Can easily have an image with only Python2, only Python3 and both - for testing.

Previously this would have involved hacks and work-arounds. 

### Deployment use-case

* Once i2c is configured on the base system, nothing needs to be installed on top at all
* Everything can be installed straight into the image - even at different versions
* Can be used as a base image to be derived from for a personal project with scroll-phat

### Can be used to distribute a tested/working installation

* Maintainer builds image
* Maintainer uploads to Docker Hub
* Consumer/enthusiast pulls image, runs exactly the same as it did for the maintainer.

