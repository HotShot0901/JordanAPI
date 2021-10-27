import datetime
from collections import deque
from abc import ABC
from threading import Thread

class queue(deque):
    '''
    The queue class used.
    Recomenderd to user not mess with it.
    '''

    def push(self, item) -> None:
        '''
        Used to push element to the queue.
        Appends the item to the end of the queue.
        '''

        self.append(item)

    def pop(self):
        '''
        Used to pop items from the queue.
        Pops the first element (From left) of the queue.
        '''

        return self.popleft()

class Logger():
    def __init__(self, saveLog: bool=False, logFileAddress: str=".", program: str="Host", timestamp: bool=False) -> None:
        '''
        It is a fast printing library made for pyhton.
        It uses multithreading to print and save multi-color strings to console and file.

        saveLog: bool       => Weather or not to save the logs to a file.
        logFileAddress: str => The address where the log file will be made.
        program: str        => The name of the host program.
        timestamp: bool     => Weather or not to print the time at which the log was made. Formate of time is [HH:MM:SS]
        '''

        self.running = True
        self.timestamp = timestamp
        self.logThread = None

        if saveLog:
            path = "{}\\{}_Log_{}_{}.txt".format(logFileAddress, program, Logger.getTime(), Logger.getDate())
            path = path.replace(":", "-")
            self.logFile = open(path, 'w')

        else:
            self.logFile = None

        self.logQueue = queue()

        def logThreadFunc(self):
            while self.running:
                try:
                    msg, msgColored = self.logQueue.pop()
                    print(msgColored)

                    if self.logFile != None:
                        self.logFile.write(msg + "\n")

                except:
                    continue

        self.logThread = Thread(target=logThreadFunc, args=(self,))
        self.logThread.start()

        welcomeMsg = "{}\nStarting Logger at {} for {}\n".format(Logger.getDate(), Logger.getTime(), program)

        _ts = self.timestamp
        self.timestamp = False
        self.log(welcomeMsg)
        self.timestamp = _ts

    def log(self, text: str, level=None) -> None:
        '''
        Used to log stuff.

        text: str => The text you want to Log
        level: Logger.LogLevel => The sevearity of log. Various log levels are avaiable in Logger.LogLevel class.
        '''

        def _log(self, text, level=None):
            if level == None:
                level = Logger.LogLevel.Normal

            if self.timestamp:
                text = "[{}] {}".format(Logger.getTime(), text)

            textColored = Logger.LogColors.autoColor(level, text)
            self.logQueue.push((text, textColored))
        
        logT = Thread(target=_log, args=(self, text, level))
        logT.start()

    def logSuccess(self, text) -> None:
        '''
        Alise to logger.log(text, Logger.LogLevel.Success)
        '''

        self.log(text, Logger.LogLevel.Success)

    def logWarning(self, text) -> None:
        '''
        Alise to logger.log(text, Logger.LogLevel.warning)
        '''

        self.log(text, Logger.LogLevel.warning)

    def logError(self, text) -> None:
        '''
        Alise to logger.log(text, Logger.LogLevel.Error)
        '''

        self.log(text, Logger.LogLevel.Error)

    def stop(self):
        '''
        Stops the Logger and the printing Thread.
        '''

        while True:
            if (len(self.logQueue) == 0): 
                self.running = False
                break
            
            else:
                continue
            
        self.logThread.join()

        if self.logFile != None:
            self.logFile.close()

    def halt(self):
        '''
        Stops the Logger and the printing Thread.
        '''

        self.running = False
            
        self.logThread.join()

        if self.logFile != None:
            self.logFile.close()

    class LogLevel(ABC):
        '''
        Used to specify the Level of the Log.\n
        Basicly it changes the color of the text.

        @param Normal = white\n
        Success = green\n
        warning = yellow\n
        Error = red
        '''

        Normal = "white"        # Colors the string White
        Success = "green"       # Colors the string Green
        warning = "yellow"      # Colors the string Yellow
        Error = "red"           # Colors the string Red

    class LogColors(ABC):
        '''
        The functions in this Class is used to Color Unicode strings.
        '''

        def autoColor(name: str, text: str) -> str:
            '''
            Automaticly choses the color to paint the String.
            The name varible is of type Logger.LogLevel
            '''

            dic = {
                "white": Logger.LogColors.white,
                "green": Logger.LogColors.green,
                "yellow": Logger.LogColors.yellow,
                "red": Logger.LogColors.red
            }

            return dic[name](text)

        def white(text) -> str:
            '''Colors the string White'''

            return text

        def green(text) -> str:
            '''Colors the string Green'''
            
            return "\033[92m{}\033[00m".format(text)

        def yellow(text) -> str:
            '''Colors the string Yellow'''
            
            return "\033[93m{}\033[00m".format(text)

        def red(text) -> str:
            '''Colors the string Red'''
            
            return "\033[91m{}\033[00m".format(text)

    @staticmethod
    def getTime() -> str:
        '''
        Return the current time in { HH:MM:SS } format.
        '''

        timeData = datetime.datetime.now()
        s = timeData.strftime("%H:%M:%S")
        return s

    @staticmethod
    def getDate() -> str:
        '''
        Return the  time in { YYYY:MM:DD } format.
        '''

        dateData = datetime.datetime.now()
        s = dateData.strftime("%Y-%m-%d")
        return s
