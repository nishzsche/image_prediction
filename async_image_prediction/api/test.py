import os
import dotenv

project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
dotenv_path = os.path.join(project_dir, ".env")
dotenv.load_dotenv(dotenv_path)

print(os.getenv("DATABASE_URL"))
