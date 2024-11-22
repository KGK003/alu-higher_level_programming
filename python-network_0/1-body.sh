#!/bin/bash
# Sends GET request and displays the appropriate message based on number of redirections
redir_count=$(curl -s -I "$1" | grep -i "HTTP/" | grep -c "3[0-9][0-9]"); [ "$redir_count" -eq 0 ] && echo "Direct access" || [ "$redir_count" -eq 1 ] && echo "With one redirection" || [ "$redir_count" -eq 5 ] && echo "With 5 redirections"
