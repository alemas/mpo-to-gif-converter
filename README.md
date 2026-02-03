Hi! I made this simple script to convert photos I take with my 3DS into stereoscopic gifs. 
Here's how to use it:
1. Not mandatory, but it is a good practice to create a virtual environment to run this script
2. Run `python3 -m pip install -r requirements.txt` to install the dependencies
3. Place your .mpo file inside the same folder as `main.py`
4. In the `main.py` script, replace the `filename` variable value with the name of your .mpo file
5. OPTIONAL: Uncomment the last 4 lines to also output a .jpg file containing the images for both eyes
6. Run the script with `python3 ./main.py`
7. A file called `stereoscopic.gif` (and one called `stereoscopic.jpg` if you followed step 5) should be generated in the same folder as the script
