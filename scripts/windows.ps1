"Archivo Windows" | Out-File windows.txt
icacls windows.txt /grant Everyone:F
Start-Process powershell -ArgumentList "Start-Sleep 2" -NoNewWindow
