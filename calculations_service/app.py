from pathlib import Path

from connexion import FlaskApp

from config import calc_config

SWAGGER_PATH = Path(__file__).absolute().parent / 'swagger.yaml'

app = FlaskApp(
    import_name=__name__,
    specification_dir=SWAGGER_PATH.parent,
    host=calc_config.host,
    port=calc_config.port,
)
app.add_api('swagger.yaml')

if __name__ == '__main__':
    app.run(debug=True)
