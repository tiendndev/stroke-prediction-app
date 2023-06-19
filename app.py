from strokeprediction import create_app
from strokeprediction import config

app = create_app()
app.config.from_object(config.config['development'])

if __name__ == "__main__":
    app.run(debug=True)
