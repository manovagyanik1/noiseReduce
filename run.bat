mkdir cleanVideo

for /r %%i in (*) do (
	set fileextension=%%~xi
	if fileextension == '.mp4' (
			sh noiseClean.sh %%i cleanVideo/%%i
		)
	)