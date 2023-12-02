# AoC 12-01

getFirstDigit () {
  pcre2grep -o1 '^.*?(\d)'
}

runningTotal=0

# Iterate over lines of the input file
while read line; do

  # get the first digit in the string
  d1="$( getFirstDigit <<< "$line" )"

  # get the first digit of the reversed string (last digit of original)
  d2="$( (rev | getFirstDigit) <<< "$line" )"

  # update a running total with the concatenated digits
  ((runningTotal+= 10*d1 + d2))

done < "12-01-input.txt"

echo "Sum is: $runningTotal"

