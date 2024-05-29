import os
import sys, getopt
import shutil

# Edit to choose your firmware located in c:\Users\Name\STM32Cube\Repository"
firmware_to_be_used = "STM32Cube_FW_H7_V1.11.2"

def main(argv):
    thisdir = os.getcwd() + "\\Drivers"
    print(thisdir)
    src_firmware_dir = os.path.expanduser('~') + "\\STM32Cube\\Repository\\" + firmware_to_be_used + "\\Drivers"
    print(src_firmware_dir)
    for r, d, f in os.walk(thisdir):
        for file in f:
            filename_old = os.path.join(r, file)
            filename_new = src_firmware_dir + filename_old.replace(thisdir, "");
            print (filename_new + " > "  + filename_old)
            shutil.copyfile(filename_new, filename_old)

if __name__ == "__main__":
    main(sys.argv)

