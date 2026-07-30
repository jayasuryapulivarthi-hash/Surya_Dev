[1mdiff --git a/app/db/database.py b/app/db/database.py[m
[1mindex 23c08bc..704062b 100644[m
[1m--- a/app/db/database.py[m
[1m+++ b/app/db/database.py[m
[36m@@ -7,7 +7,8 @@[m [mfrom sqlalchemy.orm import sessionmaker, DeclarativeBase[m
 [m
 class Base(DeclarativeBase):[m
     pass[m
[31m-load_dotenv()[m
[32m+[m[32mENV_FILE = os.getenv("ENV_FILE", ".env")[m
[32m+[m[32mload_dotenv(ENV_FILE)[m
 [m
 DB_USER = os.getenv("DB_USER")[m
 DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))[m
[1mdiff --git a/requirements.txt b/requirements.txt[m
[1mindex ea0a4e4..c5f62c0 100644[m
[1m--- a/requirements.txt[m
[1m+++ b/requirements.txt[m
[36m@@ -5,3 +5,5 @@[m [mpydantic[m
 psycopg[binary][m
 python-dotenv[m
 pandas[m
[32m+[m[32mpyarrow[m
[32m+[m[32malembic==1.18.5[m
\ No newline at end of file[m
