#!/bin/bash

FILE=$1 #define var for reference in loops
NUM=$2 #define car for reference in loops
if [[ $# -eq 0 ]]; then # If there is no argument input 
        printf "Usage: %s FILE [NUM]\n" "$(basename "$0")" #print usage statement 
        exit 1
else
if [[ -f "$FILE" ]]; then    #-f is testing to see if input for FILE is a file
if [[ $NUM -gt 0 ]]; then    #if NUM has input 

        i=0

	while read -r LINE; do #for each line
                let i++		#add i + 1	
                       	if [[ i -le $NUM ]]; then #if i is less than the NUM
				echo $LINE	#print the component of the line
                       	
                        else

                        break
                        fi
                        done < "$FILE"
        exit 1
else
    	i=0

	while read -r LINE; do #see above, this is our default counter for 3 lines
        let i++
               	if [[ i -le 3 ]]; then
              	 	 echo $LINE
                	
                else

                break
                fi
        done < "$FILE"
fi
else
    	printf "\"%s\" is not a file\n" "$(basename "$FILE")" #if file test fails i.e. no file, print error statement
	exit 1		
fi
fi
