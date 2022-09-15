$IP = (getIP)
$date = (get-date)
$PSVersion = $PSVersionTable.PSVersion.Major
function getIP{
    (Get-NetIPAddress).ipv4address | Select-String "192*"
}
$BODY = "This machine's IP is $IP, User is $env:USERNAME, Hostname is $env:COMPUTERNAME. Powershell version $PSVersion, Today's date is $date "
Send-MailMessage -To "sacketjr@ucmail.uc.edu" -From "jsackett2012@gmail.com" -Subject "IT3038C Windows Sysinfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSsl -Credential (Get-Credential)
