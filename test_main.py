import pytest
from click.testing import CliRunner
from library.model import classify

# test model to make sure it's working!
# since this program downloads the model directly from huggingface, the expected results may change if the model is updated.
def test_classify():
    results = classify("I love this")
    assert results[0][0].get("label") == 'anger'

if __name__ == "__main__":
    test_classify()

