import argparse
from utils import *


def main():
	# create argument parser object 
    parser = argparse.ArgumentParser(description = "Weather Reporter") 
  
    parser.add_argument("-s1", "--string1", type = str, nargs = '*', 
	                    metavar = "location", default = None, help = "Location") 
	                    
    parser.add_argument("-s2", "--string2", type = str, nargs = '*', 
	                    metavar = "location", default = None, help = "Location") 

    parser.add_argument("-d", "--days", type = int, nargs = 1, 
	                    metavar = "days", default = [1], help = "Number of days") 

	# parse the arguments from standard input 
    args = parser.parse_args()
    #print(' '.join(args.string1))
    #weather_data = get_weather(args.query, args.days[0])
    result = calculate_cer(' '.join(args.string1),' '.join(args.string2))
    #print_weather_details(weather_data)
    print(result)


if __name__ == "__main__":
    main()
