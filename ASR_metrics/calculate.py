import argparse
import utils 


def main():
	# create argument parser object 
    parser = argparse.ArgumentParser(description = "Weather Reporter") 
  
    parser.add_argument("-s1", "--string1", type = str, nargs = '*', 
	                    metavar = "first string", default = None, help = "Actual string or list of string ") 
	                    
    parser.add_argument("-s2", "--string2", type = str, nargs = '*', 
	                    metavar = "second string", default = None, help = "Predicted string of list of string") 

    parser.add_argument("-lp", "--listpair", type = str, nargs = '*', 
                        metavar = "string pair", default = None, help = "String pair of Actual and predicted [(s1,s2)]") 

    
    parser.add_argument("-d", "--days", type = int, nargs = 1, 
	                    metavar = "days", default = [1], help = "Number of days") 

	# parse the arguments from standard input 
    args = parser.parse_args()
    #print(' '.join(args.string1))
    #weather_data = get_weather(args.query, args.days[0])
    r1,r2 = 0,0
    if args.listpair is not None:
        r1 = utils.compute_wer_list_pair(args.listpair)
        r2 = utils.calculate_cer_list_pair(args.listpair)
        #return r1,r2
    else:
        r1 = utils.calculate_cer(' '.join(args.string1),' '.join(args.string2))
        r2 = utils.calculate_wer(' '.join(args.string1),' '.join(args.string2))
        
        #return r1 , r2
    #print_weather_details(weather_data)
    print("CER: {:.4f}, WER: {:.4f}".format(r1,r2))


if __name__ == "__main__":
    main()
