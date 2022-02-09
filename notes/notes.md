## Python notes

- GIL (global interpreter lock) - Python process can run only 1 instruction at the time (no matter how many cores it uses)

#### <b>Modules</b>

- module: single python file
- searching will be performed in items of sys.path
- code inside ```if __name__ == "__main__"``` block will not be run when this module will be imported by another module

- <b>PYTHONPATH</b> env variable - can be modified to add directories where imported modules will be searched (to permanent usage add it to .bashrc/.zshrc)

- several modules (python files) with <b>\_\_init\_\_.py</b> will make a <b>package</b>, then Python will know that files in directory containing init are modules

- within <b>\_\_init\_\_.py</b> we will import necessary modules from that directory (or others) - imports have to be ralative or absolute (recommended)
