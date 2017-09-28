#!/bin/bash

FILE=$1
NUM=$2
if [[ $# -eq 0 ]]; then
        printf "Usage: %s FILE [NUM]\n" "$(basename "$0")"
        exit 1
else
if [[ -f "$FILE" ]]; then
if [[ $NUM -gt 0 ]]; then

        i=0

	while read -r LINE; do
                let i++
                       	if [[ i -le $NUM ]]; then
				echo $LINE
                       	
                        else

                        break
                        fi
                        done < "$FILE"
        exit 1
else
    	i=0

	while read -r LINE; do
        let i++
               	if [[ i -le 3 ]]; then
              	 	 echo $LINE
                	
                else

                break
                fi
        done < "$FILE"
fi
else
    	printf "\"%s\" is not a file\n" "$(basename "$FILE")"
	exit 1		
fi
fi
