# AoC 12-01

# Need to recognize input like "eightwo" as "8", not "2".
# If we use sed to substitute "one", "two", etc., for their digits,
# the order of the substitution commands would give us "eigh2" and we'd
# erroneously pick up 2 as the first digit.

# So we need to look for the first occurence of a digit name.
getFirstDigit () {
  pcre2grep -o1 '^.*?(one|two|three|four|five|six|seven|eight|nine|\d)'
}

# We can't use the same function any more because "eightwo5ruof" must
# give us 85, not 84. We need a function specific to the reversal.
getFirstDigitOfReversal () {
  pcre2grep -o1 '^.*?(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)'
}

runningTotal=0

# Iterate over lines of the input file
while read line; do

  # get the first digit in the string
  d1="$( getFirstDigit <<< "$line" )"

  # get the first digit of the reversed string (last digit of original).
  # reverse it so that it's readable and ready for next step
  d2="$( (rev | getFirstDigitOfReversal | rev ) <<< "$line" )"

  # ensure only numbers are present before summing
  num="$(echo $d1$d2 | sed 's/one/1/g; s/two/2/g; s/three/3/g; s/four/4/g; s/five/5/g; s/six/6/g; s/seven/7/g; s/eight/8/g; s/nine/9/g' )"

  # update a running total with the concatenated digits
  ((runningTotal+= num))

done < "12-01-input.txt"

echo "Sum is: $runningTotal"

