#!/bin/bash
# Sends a GET request and displays output based on the number of redirects
redir_count=$(curl -s -L -I "$1" | grep -i "HTTP/" | grep -c "3[0-9][0-9]"); if [ "$redir_count" -eq 0 ]; then echo "Direct access"; elif [ "$redir_count" -eq 1 ]; then echo "With one redirection"; elif [ "$redir_count" -eq 5 ]; then echo "With 5 redirections"; fi
