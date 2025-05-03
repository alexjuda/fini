import typer


app = typer.Typer()


@app.command()
def entry():
    print("hello")

@app.command()
def entry2():
    print("hello")
