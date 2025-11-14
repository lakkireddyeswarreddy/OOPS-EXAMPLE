from datetime import datetime

class Logger:
    
    _instance = None
    
    def __new__(cls):
        
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = list()
            
        return cls._instance
    
    def log(self, message, level):
        self.logs.append(f"{datetime.now()}-{level}-{message}")
        
    def dump(self):
        for log in self.logs:
            print(log)
            
if __name__ == "__main__":
    logger1_obj = Logger()
    logger1_obj.log("hello from log level 1", "info")
    logger2_obj = Logger()
    logger2_obj.log("hello from log level 1", "info")
    
    print(logger1_obj is logger2_obj)
    print(logger1_obj.logs)
    print(logger2_obj.logs)
