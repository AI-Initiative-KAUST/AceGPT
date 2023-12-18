from transformers import GPTNeoXTokenizerFast
tokenizer = GPTNeoXTokenizerFast.from_pretrained("gpt2")
tokenizer("Hello world")["input_ids"]