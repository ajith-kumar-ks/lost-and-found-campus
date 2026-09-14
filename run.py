from app import create_app

app = create_app()

if __name__ == '__main__':  #Only start the development server if run.py is executed directly
    app.run(debug=True)