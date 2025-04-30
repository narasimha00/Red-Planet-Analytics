![image](https://github.com/user-attachments/assets/25445aef-ae68-48de-bbde-1ff6c406b186)


# Red Planet Analytics
## What is RPA?
* _Red planet Analytics_ is a python program that provides a user friendly *TUI* for analyzing NASA's Insight weather readings and recent on-situ mars pictures.

## Test/Run Instructions
**Note:** <br>
_1. Install Python from [here](python.org) for windows or from respective package manager for linux._ <br>
_2. Set up a virtual environment manually or using services like `anaconda`, `jupyter`, etc... and run/test this program and the provided commands there to avoid package version conflicts._

### For Linux

**Recommendation**: You can symlink the activate binary from your custom virtual environment directory to our project's venv folder like this <br>
```ln -s <path-to-binary> <project-root-directory>/venv/bin/activate``` <br>
generally the `<path-to-binary>` will be `<venv>/bin/activate` where `<venv>` is your virtual environment name. 

* **Step 1:** Install the requirements mentioned in `requirements.txt` using command `pip install -r <path-to-requirements.txt>`, if you're on the root project directory, you can run the following command. <br>
```
pip install -r requirements.txt
```

* **Step 2:** Run the python program using command `python <path-to-main.py>`, again you can run the following command if you're on the project's root directory or Alternatively, you can try running the `run.sh` shell script provided in the project's root directory.
```
python src/main.py
```    

## Features
* Fetch per sol Weather data recorded by NASA's Insight Lander.
* Display the 7 sols data on the variation graph.
* Fetch Recent images captured by various NASA's rovers from Mars and stich them to give a panoramatic image.
