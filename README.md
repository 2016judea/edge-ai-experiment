# edge-ai-experiment

## Install Dependencies

```
./setup.bash
```

## Run Model

```
python agent.py
```

(this assumes you are executing the AI "agent" on a Raspberry Pi with an LED connected on GPIO header pin 17...take a look at `commands.py` to see why)

## Problem Statement

I've been seeing a lot of industry demand (circa Feb '25) for what's known colliqually as "edge ai". Simply put, running AI on low power/minimum compute devices on the edge of the network (and not necessarily a server farm in Palo Alto). Which is interesting, given that most AI applications to-date have been focused on "pure software". Which naturally implies that Mom and Pop Fortune 500s are starting to recognize the application of AI within their own spaces. Especially now that the models are getting smaller/more efficient.

## Purpose

I wanted to see how feasible/useful it was to run an AI model on an edge device (my Raspberry Pi). Had to poke around a bit and get familiar with some of the new SDKs (such as GPT4All and llama.cpp) as well as find a model small enough to run on my Pi (given my Pi Zero only has ~800 MB of RAM). As it turns out, I was pleasantly surprised how efficient (and easy) it was to directly applie AI to a hardware interface. Take a look at `agent.py` to fully grasp the implications.

## References

- Llama CPP: https://pypi.org/project/llama-cpp-python/
- Hugging Face model: https://huggingface.co/QuantFactory/Qwen2-1.5B-Instruct-GGUF
