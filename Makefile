mainWindow.py : mainWindow.ui
	pyuic4 mainWindow.ui > mainWindow.py

run: main.py mainWindow.py
	./main.py
