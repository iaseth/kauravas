import json



txt_path = "kauravas.txt"
text = open(txt_path).read()
lines = [line.strip() for line in text.split("\n") if line]
kauravas_names = [line.split()[1].strip() for line in lines]
print(f"Found {len(kauravas_names)} names in {txt_path}.")

jo = {}
jo["kauravas"] = kauravas_names
json_path = "out/kauravas.json"
with open(json_path, "w") as f:
	json.dump(jo, f)

print(f"Saved: {json_path}")
