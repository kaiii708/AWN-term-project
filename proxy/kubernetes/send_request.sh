# while true; do curl -v -x socks4://192.168.49.2:31781 https://translate.google.com/;done
while true
do
date
for num in seq 1 1000000000000000000000
do
   curl -v -x socks4://192.168.49.2:32400/ https://translate.google.com/&
done
wait
done