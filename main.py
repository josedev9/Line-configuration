#imports
import cv2,imutils,argparse,textwrap,os

from additional import capture_frame,change_content
from GUI import create_window


parser=argparse.ArgumentParser(
    prog='.\main.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent("""
        ===================================================================================================
        \t\t\t\tAPPLICATION USAGE\n\n
        Line definition application and coordinates parser.
        First capture a frame to initiate the GUI for the line configuration.
        Then run the program again for the GUI to appear\n\n
        ===================================================================================================
        """))
parser.add_argument('-s','--save',type=str,help="Command to save a frame taken from the camera connected.")

args=parser.parse_args()

if args.save:
    capture_frame(name=args.save)

file=[i for i in os.listdir('.') if i.endswith(".png")]
if len(file)>1: print("Error multiple .png files detected, delete the older ones...\nExiting")
elif file: 
    points1,points2=create_window(f"{os.path.join(os.getcwd(),''.join(file))}")
    change_content(path="/home/tkeic/Documents/deepstream/counter/config_nvdsanalytics.txt",p1=points1,p2=points2)
else: raise(FileNotFoundError("Couldn't file the .png file captured from the camera so the GUI can't be initiated, stopping execution..."))


