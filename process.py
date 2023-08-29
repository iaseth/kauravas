import json



txt_path = "kauravas.txt"
text = open(txt_path).read()
lines = [line.strip() for line in text.split("\n") if line]
names = [line.split()[1].strip() for line in lines]
print(f"Found {len(names)} names in {txt_path}.")

jo = {}
jo["names"] = names
json_path = "kauravas.json"
with open(json_path, "w") as f:
	json.dump(names, f)

print(f"Saved: {json_path}")
