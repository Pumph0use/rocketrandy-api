from setuptools import setup

setup(
    name="app",
    packages=["ap"],
    include_package_data=True,
    install_requires=["flask", "flask-sqlalchemy", "flask-migrate", "flask-cors", "psycopg2", "python-dotenv"],
)
