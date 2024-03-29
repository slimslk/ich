#!/bin/bash

DIR_PATH="/opt/190224-ptm"

if [ ! -d "$DIR_PATH" ]
        then
                echo "$DIR_PATH not found"
                exit 1
fi

FILES=$(ls -p $DIR_PATH | grep -v /)
for file in $FILES
do
    if [[ "$file" == *.sh && ! -x "$file" ]]
        then
                chmod +x "$DIR_PATH/$file"
                echo "Added execution rights to file: $file"
        fi
done

echo "End of check"