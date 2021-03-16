import click
from delidog.app import api
from delidog.models import create_tables
from delidog.bot import polling
from waitress import serve
import logging


@click.group()
def cli():
    pass


@click.command(help='Creat tables in database')
def initdb():
    create_tables()


@click.command(help='Start bot')
def botpolling():
    polling()


@click.command(help='Run debug server')
@click.argument('listen', default='127.0.0.1:8000')
def runserver(listen):
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.DEBUG)

    click.echo('Run server...')
    serve(api, listen=listen)


cli.add_command(initdb)
cli.add_command(botpolling)
cli.add_command(runserver)


if __name__ == '__main__':
    cli()
