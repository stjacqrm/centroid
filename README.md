# centroid
tool to determine optimal refrerence genome given a set of fasta files

## Getting Started

### Prerequisites

What dependencies you need to run centroid.py

```
python3.6+
Mash
```

### Installing Dependencies

Installing python3.6+
First, check your version of python

```
$ python -v
```

If you don't have python3.6+, use Anaconda to install:

```
$ sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
$ wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
$ bash Anaconda3-2019.10-Linux-x86_64.sh
$ source ~/.bashrc
```

### Installing Mash

If you don't have Mash installed and set to your path, do the following:

```
$ wget https://github.com/marbl/Mash/releases/download/v2.2/mash-Linux64-v2.2.tar
$ tar -xvf mash-Linux64-v2.2.tar
$ rm -rf mash-Linux64-v2.2.tar
$ export PATH="mash-Linux64-v2.2/:$PATH"
```

### Installing centroid

To get centroid, clone this repository:

```
$ git clone https://github.com/stjacqrm/centroid.git
```

There's also a containerized version on [dockerhub](https://hub.docker.com/r/staphb/centroid). 
If you go this route, you won't have to worry about having the dependencies installed (just docker). 


### Running centroid

To run centroid if you cloned the repository:

```
$ ./centroid.py /path/to/assemblies/
```

To run centroid if you're using the docker container:

```
$  docker run --rm=True -u $(id -u):$(id -g) -v $PWD:/data centroid centroid.py assemblies/
```

## Authors

This script was originally written by Richard Stanton. I just made incredibly minor modifications for it to run using python3.6+ and to produce an output file as well as printing to the command line.


* **Richard Stanton** - *Actual author*

* **Rachael St. Jacques** - *Modifier and host for code* - [stjacqrm](https://github.com/stjacqrm)
