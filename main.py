"""
This is the main file that should be used to run the code. It uses the click library to create a CLI tool.
"""

import click

from library.model import classify

@click.command()
@click.option('--text', help='text to be classified')

def main(text): # pylint: disable=no-value-for-parameter
    #get predictions from model
    results = classify(text)
    labels = []
    scores = []
    click.echo("Results: ")

    #display results
    for result in results[0]:
        label = result.get("label")
        score = result.get("score")
        labels.append(label)
        scores.append(score)
        click.echo(click.style(f"{label}: {score}"))

    #find top result
    max_score = round(max(scores), 2) * 100
    top_emotion_index = scores.index(max(scores))
    top_emotion = labels[top_emotion_index].upper()
    click.echo(click.style(f"The top prediction is {top_emotion} with score of {max_score}%."))


if __name__ == "__main__":
    main() # pylint: disable=no-value-for-parameter
