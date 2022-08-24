from distutils.command.config import config
import typer
from ssg.site import Site

def main(source="dontent", dest="dist"):
    config = {"source": source, "dest": dest}

    Site(**config).build()

typer.run(main)  
