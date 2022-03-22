$path = "C:\Windows\System32"
$items = Get-ChildItem -Path $path
[System.Collections.ArrayList]$itemsToCompress = @()
[System.Collections.ArrayList]$itemsToNotCompress = @()
$archivefile = "test.zip"

function checkfilesize {
 param ([String]$file)
 try{
    if ((Get-Item $file).length/1GB -ige 2)
        {
		    return 0
        }
	    else{
	        return 1
	    }
    }
 catch {
    return 0
 }
}


foreach ($item in $items){
    if (checkfilesize($item.FullName))
    {
        Try {
            Write-Host $item.FullName
            # Checking File Mode and Access
            $FileStream = [System.IO.File]::Open($item.FullName,'Open','Read')
            if ($null -ne $FileStream){
                $FileStream.Close()
                $FileStream.Dispose()
                $itemsToCompress += $item.FullName
            }
        }
        Catch {
            $itemsToNotCompress += $item.FullName
        }
    }
}

$itemsToCompress | Compress-Archive -DestinationPath $archivefile -ErrorAction SilentlyContinue


