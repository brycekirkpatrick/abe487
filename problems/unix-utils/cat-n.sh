
#!/bin/bash
FILE=$1  #set variable for file, input argument 1
if [[ $# -eq 0 ]]; then #testing if the argument is present

        printf "Usage: %s FILE\n" "$(basename "$0")" #print usage statment if no argument present
        exit 1
else


    	if [[ -f "$FILE" ]]; then #testing if FILE (arg 1) is in fact a file
i=0 #setting base variable for while loop

                while read -r LINE; do #while reading the lines from the input
                let i++			#add i+1 for each iteration

                printf "$i $LINE\n" #print the value for i then the first component of input argument

                 done<"$FILE" 

        else
		printf "\"%s\" is not a file\n" "$(basename "$FILE")" #if the file test fails, print error message
		        exit 1
	fi


fi


