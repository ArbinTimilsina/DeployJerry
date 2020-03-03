BOS = '<|startoftext|>'
EOS = '<|endoftext|>'


def complete_this(
        model, tokenizer, device, seed_sequence, max_length=40
):
    seed_sequence = BOS + seed_sequence
    encoded_seed_sequence = tokenizer.encode(
        seed_sequence, add_special_tokens=False, return_tensors="pt"
    )
    encoded_seed_sequence = encoded_seed_sequence.to(device)

    output_sequences = model.generate(
        input_ids=encoded_seed_sequence,
        max_length=max_length,
        temperature=1.0,
        top_k=0,
        top_p=0.95,
        repetition_penalty=1.0,
        do_sample=True
    )

    generated_sequence = output_sequences[0].tolist()
    decoded_generated_sequence = tokenizer.decode(
        generated_sequence, clean_up_tokenization_spaces=True
    )
    decoded_generated_sequence = decoded_generated_sequence.replace('\n', ' ')\
        .replace(BOS, ' ').replace(EOS, ' ').replace('</|startoftext|>', ' ')\
        .replace('[/startoftext]', ' ')\
        .replace('<|', ' ').replace('|>', ' ').replace('< |', ' ').replace('| >', ' ')\
        .replace('</', ' ')

    index = []
    for eos in ['. ', '? ', '! ']:
        if eos in decoded_generated_sequence:
            index.append(decoded_generated_sequence.find(eos))
    if index:
        stop_index = min(index) + 1
    else:
        stop_index = len(decoded_generated_sequence)
    output = decoded_generated_sequence[:stop_index]

    return output
