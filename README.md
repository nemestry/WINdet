# WINdet (URBANCODE)

__Buildings construction detection using 3 types: windows, empty and filled by 😋RTKashi team😋__

👨‍💻HOW TO USE:

__Using python in the terminal or IDE:__

▶️Install all the python packages via link (only for Windows users): https://www.python.org

▶️Update all the python packages (for Unix-system users)

1. __Open IDE or terminal (*cd ./windet*) and create a venv:__

`python3 -m venv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt`

(for using GPU use `pip3 install --upgradge torch torchvision`)

2. __Load your data to *./private/images*__

3. __Start the script usimg IDE or type the command__

   `python3 main.py`

4. __Check the detect data in *./runs/detect/output*__

5. __Have a high level of mAP 😋😋__




![windetASHI](https://github.com/nemestry/WINdet/assets/132063573/93988e49-c047-476b-b60e-a1f3c227b641)



__Using a Docker container__

▶️Install the Docker latest version via link: https://www.docker.com

1, __Open * cd ./windet* in the terminal__

2. __Build a new Docker-image using the command:__

   `docker build -t windet .`

3. __Run the Docker-container:__

   `docker run windet`

4. __Check the results in *./runs/detect/output*__ using a Docker-app

5. __Have a high level of mAP 😋😋__

![test16](https://github.com/nemestry/WINdet/assets/132063573/5339944c-cc3e-4598-a5b4-5f1962a63e22)



