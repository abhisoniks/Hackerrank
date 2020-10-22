# In a given fragment of text, replace all parentheses ()  with box brackets  [].
#!/bin/bash
while read line
do
    echo  $line | tr "()" "[]"
done
echo $line | tr "()" "[]"

# In a given fragment of text, delete all the lowercase characters .
while read line
do
  echo $line | tr -d "a-z"
done

# In a given fragment of text, replace all sequences of multiple spaces with just one space.
while read line
do
  echo $line | tr "[:space:]" " "
done
