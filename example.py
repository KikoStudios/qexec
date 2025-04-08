from qexec import configure, register_exec, call_llm, parse_and_execute

# First, let's define some example functions that simulate home automation
def control_lights(state: bool):
    print(f"Lights turned {'ON' if state else 'OFF'}")

def toggle_lights():
    print("Lights toggled")

def set_fan_speed(speed: float):
    print(f"Fan speed set to {speed}%")


configure(
        model="meta-llama/llama-4-scout:free",
        api_key="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"
    )

    # 2. Register commands
register_exec(
        "lights-on-ir",
        control_lights,
        description="Control the lights (ON/OFF)",
        type="switch"
    )

register_exec(
        "lights-toggle-ir",
        toggle_lights,
        description="Toggle the lights",
        type="button"
    )

register_exec(
        "fan-speed",
        set_fan_speed,
        description="Set the fan speed percentage",
        type="range",
        value_range=(0, 100)
    )


response = call_llm("can you set the fan to 73 percent")
print("LLM Response:", response)
 # Execute the commands
parse_and_execute(response)

