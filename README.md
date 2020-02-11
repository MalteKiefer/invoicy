
# THIS IS STILL A DEVELOPMENT VERSION NOT FOR PRODUCTION

### Installation

```bash
git clone https://github.com/MalteKiefer/invoicy
cd invoicy
pip3 install -r requirements.txt
sudo cp data/com.github.maltekiefer.invoicy.gschema.xml /usr/share/glib-2.0/schemas/
glib-compile-schemas /usr/share/glib-2.0/schemas/
```

### Run

```bash
python3 src/main.py
```
