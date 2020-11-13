#!/bin/bash
# 
# read -p "Please enter your name :" my_name
# 
# if [ $my_name = "" ] 
# then 
# 	echo "One for you, one for me."
# else
# 	echo "One for $my_name, one for me."
# fi

if [ $# -eq 0 ] 
then 
	echo "One for you, one for me."
else 
	echo "One for $1, one for me."
fi
