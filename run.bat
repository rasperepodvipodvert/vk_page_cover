SET logfile="run.log"

@echo Starting Script at %date% %time% >> %logfile%
"C:\Program Files (x86)\Python37-32\python.exe" "E:\Projects\vk_page_cover\upload_cover.py"
@echo finished at %date% %time% >> %logfile%