import os

modules = ["requests", "pystyle", "art"]

for module in modules:
	os.system(f"pip install {module}")
print("Модули установлены")