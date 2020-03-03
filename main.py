from flask import Flask, render_template, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer

from server import complete_this

app = Flask(__name__)

DEVICE = 'cpu'
MODEL = GPT2LMHeadModel.from_pretrained('model')
MODEL.to(DEVICE)
TOKENIZER = GPT2Tokenizer.from_pretrained('model')


@app.route('/')
def get_seed():
    return render_template('for_seed.html')


@app.route('/completed', methods=['POST'])
def make_completions():
    if request.method == 'POST':
        seed_sequence = request.form['seed']
        completion = complete_this(MODEL, TOKENIZER, DEVICE, seed_sequence)

        return render_template(
            'render_this.html', seed=seed_sequence, jerry_completes=completion
            )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
