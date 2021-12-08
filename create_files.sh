current_day=$(date +%d | sed 's/^0*//')
next_challenge_day="$(($current_day + 1))"
for ((day=$next_challenge_day; day<=25; day++)); do
    echo $day
    mkdir -p day$day
    touch day$day/sample.txt
    touch day$day/input.txt
    touch day$day/solution.py
done