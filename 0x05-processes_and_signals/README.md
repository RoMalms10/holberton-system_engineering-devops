# Bash Scripting: Processes and Signals

## Purpose
* Learn what a PID is
* Learn how to find a PID
* Learn how to kill a PID
* Learn what signals are

## Files

| File Name | File Description |
| --------- | ---------------- |
| 0-what-is-my-pid | Bash script that displays its PID |
| 1-list\_your\_processes | Bash script that displays a list of currently running processes |
| 2-show\_your\_bash\_pid | Modifies `2-show_your_bash_pid` to display all lines with the word `bash` |
| 3-show\_your\_bash\_pid\_made\_easy | Bash script that displays the PID, along with the process name, of processes which name contains the word `bash` |
| 4-to\_infinity\_and\_beyond | Bash script that displays To infinity and beyond indefinitely |
| 5-kill\_me\_now | Bash script that kills `4-to_infinity_and_beyond process` with `kill`|
| 6-kill\_me\_now\_made\_easy | Bash script that kills `4-to_infinity_and_beyond process` without `kill` |
| 7-highlander | Bash script that displays `To infinity and beyond` indefinitely with a `sleep 2` in between each iteration and catches `SIGTERM` |
| 8-beheaded\_process | Bash script that kills the process `7-highlander` |
| 100-process\_and\_pid\_file | Modifes `7-highlander` to catch more signals |
