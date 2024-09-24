test-write:
	python src/-decode.py --pdf_path ./test/mypdf.pdf --output_path ./test/output.txt --regex "PACIENTE:.*" --remove_text "PACIENTE:" --verbose 
test-output:
	python src/pdf-decode.py --pdf_path ./test/mypdf.pdf --regex "PACIENTE:.*" --remove_text "PACIENTE:"
build:
	pyinstaller -F src/pdf-decode.py