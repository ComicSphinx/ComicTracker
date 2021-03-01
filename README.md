# ComicTracker
My home-made application. Time Tracker. This app may help you with your productivity.

![Image alt](https://github.com/ComicSphinx/ComicTracker/blob/main/images/intro.JPG)
![Image alt](https://github.com/ComicSphinx/ComicTracker/blob/main/images/second_step.JPG)
![Image alt](https://github.com/ComicSphinx/ComicTracker/blob/main/images/plot.JPG)

## Getting started

### Which version of python I am use to develop this app
    python 3.9 (64-bit)

### How to run
    py main.py
    
### How to bundle sources into one package
1. Previously you need to install PyInstaller and libs used in this project
>`pip install pyinstaller`

>`pip install PyQt5`

>`pip install matplotlib`
2. Make sure that your location is ComicTracker folder
3. Use one of this lines to bundle sources into one package
>`python -m PyInstaller --onefile --noconsole MainWindow.py`

>`PyInstaller --onefile --noconsole MainWindow.py`
4. Remove 'build/' directory and 'MainWindow.spec'
>`rm -r build`

> `rm MainWindow.spec`
5. Enter into the 'dist/' directory
>`cd dist`
6. Create 'database' folder
>`mkdir database`
7. Now you can move the 'dist' folder wherever you want.

    

## Development plan
1. <b>[✓]</b> ~Design of an application~
2. <b>[✓]</b> ~Timer~
3. <b>[✓]</b> ~Data organization (how to save and organize data)~
4. <b>[✓]</b> Statistics diagrams ("Today" button)
5. <b>[In process]</b> Develop auto-tests
6. Possibility to view diagrams for any day of any month ("Calendar" button)
7. Testing Stage

## Author
  - **Daniil Maslov** -
    [ComicSphinx](https://github.com/ComicSphinx)
