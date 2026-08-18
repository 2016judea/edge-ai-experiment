# Edge AI Experiment

Running a language model small enough to fit on a Raspberry Pi — and wiring its
output to a physical pin.

You say *"I'd like you to turn off the LED."* The model, running entirely on the
Pi, decides that means `turn_off_led()`. The LED goes off.

## Why

Circa February 2025 there was a lot of industry noise about "edge AI" — running
models on low-power devices at the edge of the network rather than in a datacenter.
Interesting, because AI to that point had been almost entirely a *software* story.
Companies reaching for edge deployment meant ordinary industrial operations were
starting to see AI as something that touches their own hardware.

So: how feasible is it, actually? The Pi Zero here has about 800 MB of RAM. That's
the constraint the whole experiment is built around.

It turned out to be easy — which is the finding.

## What happens

```mermaid
flowchart LR
    A["Natural language<br/><i>#quot;turn off the LED#quot;</i>"] --> B["Qwen2-1.5B<br/>Q2_K quantized · llama.cpp"]
    B --> C["JSON, schema-constrained<br/>one field: the function name"]
    C --> D["commands.py<br/>gpiozero"]
    D --> E["GPIO pin 17"]
```

Two details do most of the work:

**Quantization is what makes it fit.** Qwen2-1.5B-Instruct at Q2_K is under a
gigabyte, and it follows instructions well enough to beat some larger models at
this kind of task.

**The model is forced to emit JSON.** `create_chat_completion` takes a
`response_format` with a schema, so the output is guaranteed to be
`{"function": "..."}` rather than a sentence you have to parse. No regex, no string
matching, no prompt-begging for a clean answer — the constraint is enforced at
decode time.

That combination is why this is ~40 lines. The interesting part is that the phrasing
can be arbitrary — the model works out what's *really* being asked and maps it onto
a function name.

## Files

| File | Purpose |
|---|---|
| `agent.py` | Loads the model, prompts it, dispatches the returned function |
| `commands.py` | The functions the model can call — `turn_on_led()` / `turn_off_led()` |
| `setup.bash` | Dependency install |

## Running it

```bash
./setup.bash
python agent.py
```

Assumes a Raspberry Pi with an LED on **GPIO header pin 17** — see
`commands.py`, and [pinout.xyz](https://pinout.xyz/) for the header map. Without
the hardware, `gpiozero` will fail on import; swap `commands.py` for a pair of
`print()` calls and the rest runs anywhere.

The first run downloads the model from Hugging Face.

## References

- [llama-cpp-python](https://pypi.org/project/llama-cpp-python/)
- [Qwen2-1.5B-Instruct GGUF](https://huggingface.co/QuantFactory/Qwen2-1.5B-Instruct-GGUF)

Followed a year later by [tars-mini](https://github.com/2016judea/tars-mini), which
takes the same "AI on a Pi" premise considerably further — wake word, speech
recognition, and a voice.
