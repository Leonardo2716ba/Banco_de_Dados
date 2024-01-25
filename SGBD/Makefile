all: sistema_aeroporto.db
	python3 aeroporto.py

sistema_aeroporto.db:
	if [ ! -e "sistema_aeroporto.db" ]; then \
		touch sistema_aeroporto.db; \
		chmod +w sistema_aeroporto.db; \
		sqlite3 sistema_aeroporto.db < criar_banco.sql; \
	fi

