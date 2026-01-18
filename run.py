from app import create_app

# Chamamos a função que cria o aplicativo
app = create_app()

if __name__ == '__main__':
    # Rodamos o servidor
    app.run(debug=True)