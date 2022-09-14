$Hello = "Hello, Powershell"
$IP = getIP
Write-Host($Hello)
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
function getIP{
    (Get-NetIPAddress).ipv4address | Select-String "192*"
}
write-host("This machine's IP is $IP")
write-host("This machine's IP is {0}" -f $IP)