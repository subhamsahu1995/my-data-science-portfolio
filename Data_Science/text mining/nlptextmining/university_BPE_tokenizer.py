#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 14:59:30 2025

@author: Subham
"""

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.normalizers import Lowercase, NFD, StripAccents, Sequence
from tokenizers.decoders import BPEDecoder

# 1. Initialize the BPE model
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))

# 2. Set normalizer (e.g., lowercasing and stripping accents)
tokenizer.normalizer = Sequence([
    NFD(),
    Lowercase(),
    StripAccents()
])

# 3. Pre-tokenizer: split input text into words
tokenizer.pre_tokenizer = Whitespace()

# 4. Trainer: configure vocab size and special tokens
trainer = BpeTrainer(
    vocab_size=5000,
    min_frequency=2,
    special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
)

# 5. Prepare training data (a list of .txt files)
files = ["data.txt"]  # Replace with your actual training file path(s)

# 6. Train the tokenizer
tokenizer.train(files, trainer)

# 7. Set decoder
tokenizer.decoder = BPEDecoder()

# 8. Save the tokenizer
tokenizer.save("bpe-tokenizer.json")

# 9. Load and test the tokenizer
from tokenizers import Tokenizer

loaded_tokenizer = Tokenizer.from_file("bpe-tokenizer.json")

# Example usage
output = loaded_tokenizer.encode("Hello, how are you doing today?")
print("Tokens:", output.tokens)
print("IDs:", output.ids)
