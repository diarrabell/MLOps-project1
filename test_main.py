import pytest
from click.testing import CliRunner
from library.model import classify

# test model to make sure it's working!
# since this program downloads the model directly from huggingface, the expected results may change if the model is updated.
def test_classify():
    results = classify("I love this")
    #print(results[0][0].get("label"))
    assert results[0][0].get("label") == 'anger'
#     runner = CliRunner
#     results = runner.invoke(main, ["--text", "I love this"])
#     assert results.exit_code == 0
#     assert results.output == [[{'label': 'anger', 'score': 0.004419781267642975},
#   {'label': 'disgust', 'score': 0.0016119900392368436},
#   {'label': 'fear', 'score': 0.0004138521908316761},
#   {'label': 'joy', 'score': 0.9771687984466553},
#   {'label': 'neutral', 'score': 0.005764583125710487},
#   {'label': 'sadness', 'score': 0.002092392183840275},
#   {'label': 'surprise', 'score': 0.008528688922524452}]]

if __name__ == "__main__":
    test_classify()

