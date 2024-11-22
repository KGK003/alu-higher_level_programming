#!/bin/bash
# Sends GET request and counts redirects to display the correct message
redir_count=$(curl -s -L -I "$1" | grep -i "HTTP/" | grep -c "3[0-9][0-9]"); if [ "$redir_count" -eq 0 ]; then echo -n "Direct access"; elif [ "$redir_count" -eq 1 ]; then echo -n "With one redirection"; elif [ "$redir_count" -eq 5 ]; then echo -n "With 5 redirections"; fi
