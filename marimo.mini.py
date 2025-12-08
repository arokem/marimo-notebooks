import marimo

__generated_with = "0.18.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Minimal NiiVue

    This is a minimal example of how to run NiiVue.
    """)
    return


@app.cell
def _():
    from ipyniivue import NiiVue

    nv = NiiVue()
    nv.load_volumes([{"url": "https://niivue.com/demos/images/mni152.nii.gz"}])
    nv
    return


if __name__ == "__main__":
    app.run()
