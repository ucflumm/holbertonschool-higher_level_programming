#!/bin/bash

start=0
end=16

for i in $(seq $start $end)
do
	touch "${i}.sql"
	echo "-- File ${i}" > "${i}.sql"
done

echo "SQL files generated from ${start}.sql to ${end}.sql"
