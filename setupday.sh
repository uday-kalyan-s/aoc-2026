source .env
mkdir day$1
curl https://adventofcode.com/2025/day/$1/input -b session=$SESSION -A "udaykalyansreenivasa@gmail.com" > day$1/input.txt