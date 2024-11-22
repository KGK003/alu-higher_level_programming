#!/bin/bash
# Checks how many 3xx redirection responses are received
redir_count=$(curl -s -I "$1" | grep -i "HTTP/" | grep -c "3[0-9][0-9]"); if [ "$redir_count" -eq 0 ]; then echo "Direct access"; elif [ "$redir_count" -eq 1 ]; then echo "With one redirection"; elif [ "$redir_count" -eq 5 ]; then echo "With 5 redirections"; fi
