#!/bin/bash
# Quick system information display script

echo "================================"
echo "System Information"
echo "================================"
echo ""

echo "Hostname: $(hostname)"
echo "OS: $(uname -s)"
echo "Kernel: $(uname -r)"
echo ""

echo "CPU Info:"
if [ -f /proc/cpuinfo ]; then
    grep "model name" /proc/cpuinfo | head -1 | cut -d: -f2 | xargs
else
    echo "  CPU info not available"
fi
echo ""

echo "Memory Info:"
if command -v free &> /dev/null; then
    free -h | grep "Mem:" | awk '{print "  Total: " $2 ", Used: " $3 ", Free: " $4}'
else
    echo "  Memory info not available"
fi
echo ""

echo "Disk Usage:"
df -h / | tail -1 | awk '{print "  Total: " $2 ", Used: " $3 " (" $5 "), Available: " $4}'
echo ""

echo "Current User: $(whoami)"
echo "Uptime: $(uptime -p 2>/dev/null || uptime)"
echo ""
echo "================================"
