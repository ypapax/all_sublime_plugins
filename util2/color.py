class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def green(msg):
	print(bcolors.OKGREEN + msg+bcolors.ENDC)
def red(msg):
	print(bcolors.FAIL + msg+bcolors.ENDC)	
def blue(msg):
	print(bcolors.OKBLUE + msg+bcolors.ENDC)	
def warn(msg):
    print(bcolors.WARNING + msg+bcolors.ENDC)    


def color(msg, color):
    colorCode = colorToCode(color)
    return colorCode + msg + bcolors.ENDC

def colorToCode(x):
    return {
        'red': bcolors.FAIL,
        'green': bcolors.OKGREEN,
        'yellow': bcolors.WARNING,
        }.get(x, bcolors.FAIL)    # 9 is default if x not found