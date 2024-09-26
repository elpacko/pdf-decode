pdf-decode.exe --pdf_path mypdf.pdf --regex "PACIENTE:.*" --remove_text "PACIENTE:"
pdf-decode.exe --pdf_path mypdf.pdf --output_path output.txt --regex "PACIENTE:.*" --remove_text "PACIENTE:" --verbose
pdf-decode.exe --pdf_path mypdf.pdf --output_path output.txt --prefix "SET Nombre=" --regex "PACIENTE:.*" --remove_text "PACIENTE:" --verbose
pdf-decode.exe --pdf_path mypdf.pdf --output_path output.bat --prefix "Nombre" --regex "PACIENTE:.*" --remove_text "PACIENTE:" --output_batch --verbose