last_file=$(ls Yumana* 2>/dev/null | sort -n -t 'i' -k 2 | tail -1)

# If no file is found, start from number 1 and continue to the next number
if [ -z "$last_file" ]; then
    start=1
else
    start=$(expr "${last_file#Yumana}" + 1)
fi

# Start creating 25 files, starting from number 1 and continuing to the next number
i=$start
while [ "$i" -lt "$(($start + 25))" ]; do
    touch "Yumana$i"
    i=$(expr "$i" + 1)
done

