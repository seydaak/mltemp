# DemandForecasting

## Setup

### Development environment

The conda environment of this project is located in the root directory:

```
environment_win64.yml
```

Note: For a different OS, e.g. Linux, another environment file should be created, since not all package versions are
available for all OSs.

To create the conda environment in your local Anaconda installation (assuming Anaconda is installed using the "all users" option):

```
cd <project home>
conda env create -f environment_win64.yml
```

To update the environment file after installing new packages:

```
cd <project home>
conda env export > environment_win64.yml
```

To update the environment when *environment_win64.yml* has been changed by someone else (environment needs to be deactivated first):

```
cd <project home>
deactivate
conda env update -f environment_win64.yml
activate dna
```

To set conda environment as PyCharm interpreter:
  - Go to *File > Settings*
  - Select *Project: DemandForecasting*
  - Select *Project interpreter*
  - Click the small gear in the top right
  - Click *Add...*
  - Check radio button next to *Existing environment*
  - Click on "*...*"
  - Navigate to the following directory
    ("Show hidden paths" may need to be clicked in the header to see the ProgramData folder):
    
    ```
    C:\ProgramData\Anaconda3\envs\dna\python.exe
    ```
    
    Depending on your user setup and Windows version, it may also be located here:
    
    ```
    C:\Users\<user_name>\.conda\envs\dna\python.exe
    ```
    
    
  - Select *python.exe*
  - Click *OK* to exit the menu

  The Python interpreter should now start indexing, this may take some minutes.
  (Click on *x processes running...* in the lower part of the PyCharm screen to see the progress)

## Usage

### in command line or in your IDE

```
python -m src
```

## Configuration

All the configuration can be found in config.yml and loaded into the programm
using util/config.py

you can override per user the configuration values by adding a new file
config.$USER.yml, by default this file will not be versionned with Git.

### Docker container

```
docker build -t DemandForecasting .
docker run --rm -it DemandForecasting --help
```

## Test

We are using [tox](https://tox.readthedocs.io/en/latest/) to run
the tests in virtual env and with multiple version of python at
the same time to control if not too much dependant of a very
specific version of python.

```
tox
```

The code coverage report will be generated into `coverage_html_report/`

## Documentation

### Generation

To generate the doc, you need to have sphinx installed then:

```
cd docs/
make html
```

### Consultation

To vizualise the documentation:

```
cd /docs/build/html/
python -m http.server
```

then open your browser to <http://0.0.0.0:8000>
