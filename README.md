Based on the updated method of setting the configuration for `nosql_yorm`, I'll revise the README to reflect these changes:

---

# README for the 🚀 `nosql_yorm` Package 🧙‍♂️

## Overview 🌟

Welcome to `nosql_yorm`, a Python package that simplifies interactions with Firebase databases. It's an ORM (Object Relational Mapper) for NoSQL databases, with a special focus on Firebase. Whether you're building a small project or prototyping rapidly, `nosql_yorm` has got you covered with its local caching mechanism. 

## Key Features 🗝️

- **Firebase Integration**: Connects smoothly with Firebase, offering robust data storage solutions.
- **Caching for Small Projects**: A local caching system that's perfect for small-scale projects or testing phases.
- **Effortless Testing**: Conduct tests without affecting your production database.

## Installation 📦

Quick and easy installation:

```bash
pip install nosql_yorm
```

## Usage 🛠️

### Setting Up Configuration

Customize your setup with a YAML configuration file:

```python
from nosql_yorm.config import Config as NosqlYormConfig, set_config as set_nosql_yorm_config

# Load user-defined configuration
user_config = NosqlYormConfig(user_config_path="config.yaml")

# Apply the configuration to the package
set_nosql_yorm_config(user_config)
```

### Defining Models

Define models that map to your Firebase collections:

```python
from nosql_yorm.models import BaseFirebaseModel

class Unicorn(BaseFirebaseModel):
    collection_name = "unicorns"  # Define your collection name
    # Define other model properties here
```

### CRUD Operations

Easily manage your data with CRUD operations:

#### 🐣 Create and Save

```python
unicorn = Unicorn(name="Sparkles", magic_level="Over 9000")
unicorn.save()  # Saves to cache or Firebase based on configuration
```

#### 🔍 Read

```python
unicorn = Unicorn.get_by_id("unicorn_id")
```

#### ✏️ Update

```python
unicorn.name = "Rainbow Dash"
unicorn.save()  # Update existing document
```

#### ❌ Delete

```python
unicorn.delete()  # Removes from cache or Firebase
```

### Cache Interaction

Interact directly with the local cache:

```python
# Accessing a cached document
same_unicorn = cache_handler.get_document("Unicorns", "unicorn_id")

# Your entire cached data
cached_data = cache_handler.collections
```

### Integration with Web Frameworks

Combine `nosql_yorm` with frameworks like FastAPI to create powerful APIs:

```python
from fastapi import FastAPI, HTTPException
from models import Unicorn

app = FastAPI()

@app.put("/unicorns/{unicorn_id}")
async def update_unicorn(unicorn_id: str, unicorn_data: Unicorn):
    unicorn = Unicorn.get_by_id(unicorn_id)
    if not unicorn:
        raise HTTPException(status_code=404, detail="Unicorn not found")
    unicorn.merge(unicorn_data.dict())
    unicorn.save()
    return unicorn
```

## Contributing 🤝

Your contributions make `nosql_yorm` even better! Check our [contribution guidelines](YOUR_LINK_HERE).

## License 📜

`nosql_yorm` is open-sourced under the [MIT License](LICENSE).

---

Enjoy `nosql_yorm`, the ORM genie that streamlines your Firebase interactions and boosts your development experience! 🚀👩‍💻👨‍💻

---

This README now reflects the updated way of setting configurations using a YAML file, and demonstrates how the package can be effectively used in various scenarios, including model definition, CRUD operations, cache interactions, and web framework integration.