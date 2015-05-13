Function:
Batch processing text documents: 
	1. Character replace.
	2. Character insertion.
	3. Character deletion.
	4. files backup.
	5. Delete lines.
	6. Insert lines.

Command example:
Windows:
python text_file_handler.py -a "replace" -b "yes" -c "C:\simon\Temp\config_file\backup" -d ".bak" -e "C:\simon\Temp\config_file\cfg" -f "*.cfg" -g "nrOfNormalSessions := 0," -i "nrOfNormalSessions := 2,"

python text_file_handler.py -a "delete_line" -b "no" -e "C:\simon\Temp\titansim37_after" -f "*.cfg" -g "/template/REGISTER.txt" -k "1"

Linux:
python text_file_handler.py -a "insert_line" -b "no" -e "/home/ttcn3/elingyu/scripts/titansim_scripts" -f "*.cfg" -g "trafficSpecific := {" -j "src.txt"

python text_file_handler.py -a "delete_line" -b "no" -e "/home/ttcn3/elingyu/scripts/titansim_scripts" -f "*.cfg" -g "/template/REGISTER.txt" -k "1"

Parameters:
-a: Action.(replace; insert; delete; insert_line; delete_line)
-b: Backup the old files.(yes; no)
-c: Backup directory.
-d: Backup file suffix.
-e: file directory.
-f: file suffix.
-g: Origin characters.
-i: target characters.
-j: target characters file.
-k: delete line number.


