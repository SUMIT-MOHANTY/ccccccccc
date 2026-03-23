echo "Checking for available ports..."
for port in 5173 5174 5175 5176 5177 5178 5179 5180; do
    if ! netstat -tuln 2>/dev/null | grep -q ":$port " && ! ss -tuln 2>/dev/null | grep -q ":$port "; then
        echo " Port $port is available"
        break
    else
        echo " Port $port is in use"
    fi
done
