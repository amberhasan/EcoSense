#!/usr/bin/env bash
# wait-for-it.sh script

host=$1
shift
port=$1
shift
cmd="$@"

while ! nc -z "$host" "$port"; do
  echo "Waiting for $host:$port..."
  sleep 1
done

echo "$host:$port is available!"
exec $cmd
