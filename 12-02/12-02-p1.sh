# Set up maxima
redMax=12
greenMax=13
blueMax=14

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
runningGameIdTotal=0

while read game; do

	# break a game into its draws
	while read -u 3 draw ; do

		r="$(getReds <<< "$draw")"
		g="$(getGreens <<< "$draw")"
		b="$(getBlues <<< "$draw")"

		# Move on to the next game as soon as a draw is seen to be impermissible
		if [[ ( $r -gt $redMax ) || ( $g -gt $greenMax ) || ( $b -gt $blueMax ) ]]; then
			continue 2
		fi

	done 3<<< "$(gameToDraws <<< "$game" )"

	# Otherwise, the game is valid and we add the ID to our running total 
	gameID="$(pcre2grep -o1 '^Game (\d+)' <<< "$game" )"		
	((runningGameIdTotal+=gameID))

done < "12-02-input.txt"

echo "Sum is: $runningGameIdTotal"

