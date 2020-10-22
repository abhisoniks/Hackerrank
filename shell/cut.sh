#Given  lines of input, print the  character from each line as a new line of output.
#It is guaranteed that each of the  lines of input will have a  character.

#!/bin/bash
while read line
do
 echo $line | cut -b 3
done

# Display the first four characters from each line of text.
while read line
do
  echo $line | cut -b -4
done

# Display the 2  and  7th character from each line of text.
while read line
do
  echo $line | cut -b 2,7
done

# Display a range of characters starting at the  position of a string and ending at the  position (both positions included).
while read line
do
  echo $line | cut -b 2-7
done

# Print the characters from thirteenth position to the end.
while read line
do
  echo $line | cut -b 13-
done

# Given a sentence, identify and display its fourth word. Assume that the space (' ') is the only delimiter between words.
while read line
do
  echo $line | cut -b 13-
done

# Given a sentence, identify and display its fourth word. Assume that the space (' ') is the only delimiter between words.
while read line
do
  echo $line | cut -d " " -f 4
done

# Given a sentence, identify and display its first three words. Assume that the space (' ') is the only delimiter between words.
while read line
do
  echo $line | cut -d " " -f -3
done

# Given a tab delimited file with several columns (tsv format) print the fields from second fields to last field.
IFS=""
while read line
do
  echo $line | cut -f 2-
done
