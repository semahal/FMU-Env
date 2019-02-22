# FMU-Env

An [OpenAI gym](https://github.com/openai/gym) environment suitable for running a simulation model exported as FMU (Functional Mock-Up Unit). As an example, the environment is implemented for an inverted pendulum simulation model but the environment can be modified to fit other [FMI](https://fmi-standard.org/) compliant simulation models. This implementation minimizes simulation time by only running necessary methods (e.g. initialization) when absolutely needed.

## Getting Started
Below the method for integrating this environment into OpenAI Gym is described. 

### Prerequisites
Install pyFMI through the following conda* package.
```
conda install -c chria pyfmi 
```
*Requires conda package manager, install [Anaconda](https://www.anaconda.com/) and create a virtual python environment.


Install OpenAI Gym by cloning their Git repo:
```
git clone https://github.com/openai/gym.git
cd gym
pip install -e .
```



### Installing

The environment must be registered in OpenAI Gym. [This comment by hholst80](https://github.com/openai/gym/issues/626#issuecomment-310642853) provides an example.


## Test your environment

To confirm a working installation, run the testscript. 

```
>python TestRun.py
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

* Thanks to Gabriel Eyyi and his work on [dymola models in OpenAI](https://github.com/eyyi/dymrl)
