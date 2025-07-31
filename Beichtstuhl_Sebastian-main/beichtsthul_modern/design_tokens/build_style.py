import json, re, pathlib

# Get the directory of the current script to build absolute paths
script_dir = pathlib.Path(__file__).parent

# Load design tokens
tokens_path = script_dir / "design_tokens.json"
with open(tokens_path, "r", encoding="utf-8") as f:
    toks = json.load(f)

# Function to create a qlineargradient string
def grad(c1, c2):
    return f"qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 {c1}, stop:1 {c2})"

# Add gradients to the tokens dictionary
toks["gradients"] = {
    "neon_primary": grad(toks["colors"]["accent"]["1"], toks["colors"]["accent"]["2"])
}

# Add px suffix to radius values
toks["radius"]["smpx"] = str(toks["radius"]["sm"]) + "px"
toks["radius"]["mdpx"] = str(toks["radius"]["md"]) + "px"

# Add font size values
if "fonts" in toks and isinstance(toks["fonts"], dict) and "headline" in toks["fonts"]:
    toks["fonts"]["headline"]["sizes"]["h1px"] = str(toks["fonts"]["headline"]["sizes"]["h1"]) + "px"
    toks["fonts"]["headline"]["sizes"]["h2px"] = str(toks["fonts"]["headline"]["sizes"]["h2"]) + "px"
    toks["fonts"]["headline"]["sizes"]["h3px"] = str(toks["fonts"]["headline"]["sizes"]["h3"]) + "px"
    toks["fonts"]["headline"]["sizes"]["h4px"] = str(toks["fonts"]["headline"]["sizes"]["h4"]) + "px"
if "fonts" in toks and isinstance(toks["fonts"], dict) and "body" in toks["fonts"]:
    toks["fonts"]["body"]["sizes"]["bodypx"] = str(toks["fonts"]["body"]["sizes"]["body"]) + "px"
    toks["fonts"]["body"]["sizes"]["captionpx"] = str(toks["fonts"]["body"]["sizes"]["caption"]) + "px"
if "fonts" in toks and isinstance(toks["fonts"], dict) and "mono" in toks["fonts"]:
    toks["fonts"]["mono"]["sizes"]["defaultpx"] = str(toks["fonts"]["mono"]["sizes"]["default"]) + "px"

# Add px suffix to effect values
if "effects" in toks and isinstance(toks["effects"], dict) and "glass" in toks["effects"]:
    toks["effects"]["glass"]["blurpx"] = str(toks["effects"]["glass"]["blur"]) + "px"
if "effects" in toks and isinstance(toks["effects"], dict) and "glow" in toks["effects"]:
    toks["effects"]["glow"]["blurpx"] = str(toks["effects"]["glow"]["blur"]) + "px"

# Read the template file
template_path = script_dir / "style_template.qss"
tpl = template_path.read_text(encoding="utf-8")

# Replace placeholders with token values using eval
# This is safe because we control the input (the template and the tokens)
out = re.sub(r"\$([A-Za-z0-9_\.]+)",
             lambda m: str(eval("toks['" + m.group(1).replace('.', "']['") + "']")),
             tpl)

# Write the output to app.qss
output_path = script_dir / "app.qss"
output_path.write_text(out, encoding="utf-8")

print(f"Successfully generated {output_path}")