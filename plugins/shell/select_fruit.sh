FRUIT=$1
if [ $FRUIT == APPLE ]; then
	echo "You selected an Apple!"
elif [ $FRUIT == ORANGE ]; then
	echo "You selected an Orange!"
elif [ $FRUIT == GRAPE ]; then
	echo "You selected Grape!"
else 
	echo "You selected others!"
fi
