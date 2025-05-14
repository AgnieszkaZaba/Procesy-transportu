"""Tests prepared for checking some of the requirements for code format
Classes: Procesy transportu w środowisku"""

import pytest
import nbformat

PLOT=False

@pytest.fixture(name="notebook_filename")
def notebook_filename_fixture():
    """insert you file path here"""
    return "radiation.ipynb"

class TestCodeFormat:
    """Tests for cells in jupyter notebooks"""
    @staticmethod
    def test_first_cell_is_markdown(notebook_filename):
        """checks if notebook has a markdown cell in the first position that is not empty"""
        with open(notebook_filename, encoding="utf8") as file:
            notebook = nbformat.read(file, nbformat.NO_CONVERT)
            assert len(notebook.cells) > 0
            assert notebook.cells[0].cell_type == "markdown"
            lines = notebook.cells[0].source.split("\n")
            assert len(lines) > 0

    @staticmethod
    def test_comments_in_code(notebook_filename):
        """test if there is no comments in notebook"""
        with open(notebook_filename, encoding="utf8") as file:
            notebook = nbformat.read(file, nbformat.NO_CONVERT)
            for cell in notebook.cells:
                if cell.cell_type == "code" and '#' in cell.source:
                    raise AssertionError(
                        f"Comment found in a code cell {cell.source}"
                    )
    @staticmethod
    def test_no_errors_or_warnings_in_output(notebook_filename):
        """checks if notebook have clear std-err output
        (i.e., no errors or warnings) visible"""
        with open(notebook_filename, encoding="utf8") as file:
            notebook = nbformat.read(file, nbformat.NO_CONVERT)
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
