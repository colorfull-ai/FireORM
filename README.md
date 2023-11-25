# README for the 🚀 `nosql_yorm` Package 🧙‍♂️

## Overview 🌟

Hey there, clever clogs! Welcome to `nosql_yorm`, the Python package that's practically doing cartwheels to make your life easier when dabbling with Firebase databases. Think of it as your personal ORM (Object Relational Mapper) genie 🧞‍♂️ for NoSQL databases, especially Firebase. Oh, and guess what? It's got a nifty little trick up its sleeve for small projects and quick prototyping - a local caching system! Neat, huh?

## Key Features 🗝️

- **Firebase's BFF**: Hooks you up with Firebase for data storage. It's like a match made in database heaven! 💑
- **Sneaky Cache Mode**: Got a small project or just testing? Use the built-in cache so you won't bother the big ol' Firebase. 🕵️‍♂️
- **Testing Like a Boss**: Test your app without the fear of messing up your actual data. Be bold, my friend! 🦸‍♀️
- **TypeScript? Yes, Please!**: For the cool kids who love TypeScript, we've got your back. 🤘

## Installation 📦

Just a line away:

```bash
pip install nosql_yorm
```

## Usage 🛠️

### Defining Models

Modeling time! Define your Firebase models like a pro:

```python
from nosql_yorm.models import BaseFirebaseModel

class Unicorn(BaseFirebaseModel):
    collection_name = "unicorns"  # Because why not?
    # Add your magical fields here
```

### CRUD Operations

Let's do the data dance - Create, Read, Update, Delete:

#### 🐣 Create and Save

```python
unicorn = Unicorn(name="Sparkles", magic_level="Over 9000")
unicorn.save()
```

#### 🔍 Read

```python
unicorn = Unicorn.get_by_id("unicorn_id")
```

#### ✏️ Update

```python
unicorn.name = "Rainbow Dash"
unicorn.save()
```

#### ❌ Delete

```python
unicorn.delete()
```

### Testing with Cache 🤫

Shh... it's test mode. We use a secret cache:

```python
from nosql_yorm.config import set_library_config

# Psst... enable test mode
set_library_config(read_write_to_cache=True)

# Go on, run your sneaky tests here
```

### Web Endpoints Integration 🕸️

`nosql_yorm` + FastAPI = A match made in API heaven:

```python
from fastapi import FastAPI, HTTPException
from models import Unicorn

app = FastAPI()

@app.put("/unicorns/{unicorn_id}")
async def update_unicorn(unicorn_id: str, unicorn_data: Unicorn):
    unicorn = Unicorn.get_by_id(unicorn_id)
    if not unicorn:
        raise HTTPException(status_code=404, detail="Unicorn not found 😢")
    unicorn.merge(unicorn_data.dict())
    unicorn.save()
    return unicorn
```

## Another Example 🎉

Let's play with a new model:

```py
from nosql_yorm.models import BaseFirebaseModel
from nosql_yorm.config import set_library_config

set_library_config(read_write_to_cache=True)

class FancyModel(BaseFirebaseModel):
    example_field: str

# Look ma, no database!
print(FancyModel.get_all())

# Delete them all? Why not!
for Fancy in FancyModel.get_all():
    Fancy.delete()

# Create a new fancy model
fancy_model = FancyModel(example_field="fancy_data")
fancy_model.save()

# Asserting like we know what we're doing
assert fancy_model.example_field == "fancy_data"
assert fancy_model.id is not None

# Presto! Retrieve it back
fancy_retrieved = FancyModel.get_by_id(fancy_model.id)
assert fancy_model == fancy_retrieved
```

## Contributing 🤝

Wanna be part of the cool kids' club? Contributions are like gold dust! Check out our [guidelines](YOUR_LINK_HERE).

## License 📜

`nosql_yorm` is all yours under the [MIT License](LICENSE). Use it wisely! 😉

---

So, there you have it, folks! The `nosql_yorm` package in all its glory. Go forth and conquer those Firebase databases with ease and maybe a little swagger! 🚀👩‍💻👨‍💻
