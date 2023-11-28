import json
import os
from typing import Any, Dict, List, Optional

from nosql_yorm.config import get_config

class CacheHandler:
    def __init__(self, output_dir='db_output', filename='cache.json'):
        self.collections: Dict[str, Dict[str, Any]] = {}  # Mocked Firebase Store
        self.output_dir = output_dir
        self.filename = filename
        self.load_cache()  # Load existing cache data on initialization

    def save_cache(self):
        if get_config().get("persist_cache_as_db", False):
            os.makedirs(self.output_dir, exist_ok=True)
            file_path = os.path.join(self.output_dir, self.filename)
            with open(file_path, 'w') as f:
                json.dump(self.collections, f)

    def load_cache(self):
        if get_config().get("persist_cache_as_db", False):
            print("Loading cache...")
            file_path = os.path.join(self.output_dir, self.filename)
            print(f"Loading cache from {file_path}")
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    self.collections = json.load(f)

    def add_document(self, collection_name: str, document_id: str, data: Dict[str, Any]) -> None:
        if collection_name not in self.collections:
            self.collections[collection_name] = {}
        self.collections[collection_name][document_id] = data
        self.save_cache()

    def get_document(self, collection_name: str, document_id: str) -> Optional[Dict[str, Any]]:
        return self.collections.get(collection_name, {}).get(document_id)

    def update_document(self, collection_name: str, document_id: str, data: Dict[str, Any]) -> None:
        if collection_name in self.collections and document_id in self.collections[collection_name]:
            self.collections[collection_name][document_id].update(data)
            self.save_cache()

    def delete_document(self, collection_name: str, document_id: str) -> None:
        if collection_name in self.collections and document_id in self.collections[collection_name]:
            del self.collections[collection_name][document_id]
            self.save_cache()

    def list_collection(self, collection_name: str) -> List[Dict[str, Any]]:
        return list(self.collections.get(collection_name, {}).values())

    def query_collection(self, collection_name: str, query_params: Optional[Dict[str, Any]] = None) -> List[Dict]:
        all_docs = self.list_collection(collection_name)
        if not query_params:
            return all_docs

        filtered_docs = [doc for doc in all_docs if all(doc.get(key) == value for key, value in query_params.items())]
        return filtered_docs

    def clear_all_data(self) -> None:
        self.collections.clear()
        self.save_cache()

# Create an instance of CacheHandler for use in tests
cache_handler = CacheHandler()
