# Define helper functions
getReds () {
	pcre2grep -o1 '(\d+) red'
}

getGreens () {
	pcre2grep -o1 '(\d+) green'
}

getBlues () {
	pcre2grep -o1 '(\d+) blue'
}

gameToDraws () {
	pcre2grep -o '(\d+ ).*?(;|$)'
}

# Initialize valid game ID total
runningPowerTotal=0

while read game; do

	# Minima are a priori all zero
	minRed=0; minGreen=0; minBlue=0

	# Break a game into its draws
	while read -u 3 draw ; do

		# Compute colour values for the draw
		r="$(getReds <<< "$draw")"
		g="$(getGreens <<< "$draw")"
		b="$(getBlues <<< "$draw")"

		# Update the game minimum if the drawn number exceeds it
		if [[ ( $r -gt $minRed ) ]]; then minRed=$r ; fi
		if [[ ( $g -gt $minGreen ) ]]; then minGreen=$g ; fi
		if [[ ( $b -gt $minBlue ) ]]; then minBlue=$b ; fi

	done 3<<< "$(gameToDraws <<< "$game" )"

	# Compute the game's power and augment running power total
	gamePower=$((minRed * minGreen * minBlue))
	((runningPowerTotal+=gamePower))

done < "12-02-input.txt"

echo "Sum of powers is: $runningPowerTotal"

