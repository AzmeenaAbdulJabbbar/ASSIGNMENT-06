class Logger:
    def __init__(self):
        print("Object created: Logger instance is now active.")
    
    def __del__(self):
        print("Object destroyed: Logger instance is now being deleted.")
log1 = Logger()
del log1  
