# https://www.reddit.com/r/dailyprogrammer/comments/2kh2tz/10272014_challenge_186_easy_admin_schmadmin/

#These are all for powershell environments:

def task_one():
    return ' gci "C:\" -Recurse | sort LastWriteTime | select -last 20 > "<OutputPath>\MostRecentFiles.txt" '

def task_two():
    return ' gci "C:\" -Recurse | sort LastWriteTime | select -last 20 > "<OutputPath>\MostRecentFiles.txt" '
    
def task_three():
    return 'Get-History | select -last 10'
    
def task_four():
    return ' Get-WmiObject Win32_PerfFormattedData_PerfProc_Process | where-object{ $_.Name -ne "_Total" -and $_.Name -ne "Idle"} | Sort-Object PercentProcessorTime -Descending | select -First 10 | Format-Table Name,IDProcess,PercentProcessorTime -AutoSize '
    
def task_five():
    return ' get-eventlog -newest 20 -LogName System -EntryType Error | ConvertTo-Html > "<OutputPath>\MostRecentErrors.html" '

def task_six():
    return ' gci "C:\" -Recurse -include *.txt,*.pdf,*.exe '