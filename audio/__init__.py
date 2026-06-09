import platform

if platform.system() == "Linux":
    from .linux import *
else:
    from .windows import *
