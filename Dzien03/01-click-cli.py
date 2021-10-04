
# Parsowanie linii poleceń z wykorzytsaniem biblioteki click
import click

@click.command()
@click.argument("location")
@click.option("--apikey", "-a", help="klucz API")
@click.option("--humidity", is_flag=True)
@click.option("--numbers", default=1, type=int)
@click.option("--range", nargs=2, type=(int,int), default=[-1,1] )
@click.option("--verbose", "-v", count=True)
@click.option("--units", type=click.Choice(['IMPERIAL','METRIC'], case_sensitive=False), default='METRIC' )
def main(location, apikey, humidity, units, numbers, range, verbose):
    print(f"Location={location}")
    print(f"apikey={apikey}")
    print(f"humidity={humidity}")
    print(f"units={units}")
    print(f"numbers={numbers}")
    print(f"range={range}")
    print(f"verbose={verbose}")

if __name__ == "__main__":
    main()