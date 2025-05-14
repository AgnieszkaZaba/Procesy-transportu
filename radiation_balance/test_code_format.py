import pytest
import nbformat

from open_atmos_jupyter_utils import notebook_vars

PLOT=False

@pytest.fixture
def notebook_filename():
    return "my_notebook_name.ipynb"

@pytest.fixture
def notebook_variables(notebook_filename):
    return notebook_vars(
        notebook_filename, plot=PLOT
    )

class TestCodeFormat:
    @staticmethod
    def test_first_cell_is_markdown(notebook_filename):
        """checks if notebook has a markdown cell in the first position that is not empty"""
        with open(notebook_filename, encoding="utf8") as fp:
            nb = nbformat.read(fp, nbformat.NO_CONVERT)
            assert len(nb.cells) > 0
            assert nb.cells[0].cell_type == "markdown"
            lines = nb.cells[0].source.split("\n")
            assert len(lines) > 0

    @staticmethod
    def test_comments_in_code(notebook_filename):
        """test if there is no comments in notebook"""
        with open(notebook_filename, encoding="utf8") as fp:
            nb = nbformat.read(fp, nbformat.NO_CONVERT)
            for cell in nb.cells:
                if cell.cell_type == "code" and '#' in cell.source:
                    raise AssertionError(
                        f"Comment found in a code cell {cell.source}"
                    )
    @staticmethod
    def test_no_errors_or_warnings_in_output(notebook_filename):
        """checks if notebook have clear std-err output
        (i.e., no errors or warnings) visible"""
        with open(notebook_filename, encoding="utf8") as notebook_file:
            notebook = nbformat.read(notebook_file, nbformat.NO_CONVERT)
            for cell in notebook.cells:
                if cell.cell_type == "code":
                    for output in cell.outputs:
                        if "name" in output and output["name"] == "stderr":
                            raise AssertionError(output["text"])

    @staticmethod
    def test_no_for_loops_with_plots(notebook_filename):
        """check if plots and simulations are in different cell;
        but it is done with checking 'for' loops in same cell"""
        with open(notebook_filename, encoding="utf8") as notebook_file:
            notebook = nbformat.read(notebook_file, nbformat.NO_CONVERT)
            for cell in notebook.cells:
                if cell.cell_type == "code":
                    for output in cell.outputs:
                        if output.output_type == "display_data":
                            assert 'for' not in cell.source