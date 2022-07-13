import sys
import Images

System = sys.platform
print(System)

if System == "linux":
    Images.OperatingSystem.linux()
elif System == "win32" or "win64":
    Images.OperatingSystem.windows()