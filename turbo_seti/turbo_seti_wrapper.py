import os
import time
from pathlib import Path
from turbo_seti.find_doppler.find_doppler import FindDoppler
from blimpy import Waterfall
import pylab as plt
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('in_path', type=str, 
        help='Path to h5 files')
    args = parser.parse_args()
    
    in_path=args.in_path
    
    input_path=Path(in_path)
    
    # Get ready for search by  the doppler object.
    doppler = FindDoppler(str(input_path),max_drift = 7,min_drift=0, snr = 10,
                          out_dir = str(input_path.parent),
                          blank_dc=True)
    
    #start the search
    print('\n')
    print('Running the search now')
    t1 = time.time()
    doppler.search()
    
    #Produce the png plots of the hits
    print('\n')
    print('Producing the plots of the hits in png format')
    #This line is for the terminal execution of the code
    console = "plotSETI -f 3 -o " + str(input_path.parent) + " " + str(input_path.parent)
    os.system(console)
    
    #Produce the waterfall plot of the full data instead of only hits
    blimpy_object=Waterfall(str(input_path))
    plt.figure(figsize=(10,10))
    blimpy_object.plot_waterfall()
    plt.savefig('waterfall_{}_.jpg'.format(str(input_path.stem)))
