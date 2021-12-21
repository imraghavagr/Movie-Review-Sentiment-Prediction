conda-update:
	conda env update --prune -f environment.yml

piptools:
	pip-compile req.in
	pip-sync requirements.txt

app-run:
	streamlit run app.py