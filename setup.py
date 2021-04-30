from setuptools import setup

setup(
    name="bot",
    packages=["bot"],
    include_package_data=True,
    install_requires=["flask", "flask-sqlalchemy", "flask-migrate", "flask-cors", "psycopg2", "python-dotenv"],
)
