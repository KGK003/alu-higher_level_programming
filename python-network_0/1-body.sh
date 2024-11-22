#!/bin/bash
# Sends GET request and displays the correct message based on redirection count
redir_count=$(curl -s -o /dev/null -w "%{redirect_count}" "$1"); [ "$redir_count" -eq 0 ] && echo "Direct access" || [ "$redir_count" -eq 1 ] && echo "With one redirection" || [ "$redir_count" -eq 5 ] && echo "With 5 redirections"
