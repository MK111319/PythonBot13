# MK PythonBot 13

import glob
from pathlib import Path
from MKSpam.utils import load_plugins
import logging
from . import Mig, Mig2, Mig3, Mig4, Mig5, Mig6, Mig7, Mig8, Mig9, Mig10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "MKSpam/plugins/*.py"
Files = glob.glob(path)
for name in Files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("MK X Spam Successfully Deployed !!")


if __name__ == "__main__":
    Mig.run_until_disconnected()
    
if __name__ == "__main__":
    Mig2.run_until_disconnected()

if __name__ == "__main__":
    Mig3.run_until_disconnected()
    
if __name__ == "__main__":
    Mig4.run_until_disconnected()

if __name__ == "__main__":
    Mig5.run_until_disconnected()
    
if __name__ == "__main__":
    Mig6.run_until_disconnected()
    
if __name__ == "__main__":
    Mig7.run_until_disconnected()

if __name__ == "__main__":
    Mig8.run_until_disconnected()
    
if __name__ == "__main__":
    Mig9.run_until_disconnected()

if __name__ == "__main__":
    Mig10.run_until_disconnected()    
