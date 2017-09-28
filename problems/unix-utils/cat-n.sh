
#!/bin/bash
FILE=$1
if [[ $# -eq 0 ]]; then

        printf "Usage: %s FILE\n" "$(basename "$0")"
        exit 1
else


    	if [[ -f "$FILE" ]]; then
i=0

                while read -r LINE; do
                let i++

                printf "$i $LINE\n"

                 done<"$FILE"

        else
		printf "\"%s\" is not a file\n" "$(basename "$FILE")"
		        exit 1
	fi


fi


