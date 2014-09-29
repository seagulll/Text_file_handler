Function:
Batch processing text documents: 
	1. Character replace.
	2. Character insertion.
	3. Character deletion.
	4. files backup.

Command example:
python text_file_handler.py -a "replace" -b "yes" -c "C:\simon\Temp\config_file\backup" -d ".bak" -e "C:\simon\Temp\config_file\cfg" -f "*.cfg" -g "nrOfNormalSessions := 0," -i "nrOfNormalSessions := 2,"

Parameters:
-a: Action.(replace; insert; delete)
-b: Backup the old files.(yes; no)
-c: Backup directory.
-d: Backup file suffix.
-e: file directory.
-f: file suffix.
-g: Origin characters.
-i: target characters.