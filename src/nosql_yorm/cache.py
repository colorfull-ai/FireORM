import json
import os
from typing import Any, Dict, List, Optional

from nosql_yorm.config import get_config

class CacheHandler:
    def __init__(self, output_dir='db_output', filename='cache.json'):
        self.namespaces: Dict[str, Dict[str, Dict[str, Any]]] = {}  # Namespaced collections
        self.output_dir = output_dir
        self.filename = filename
        self.load_cache()  # Load existing cache data on initialization

    def set_output_dir(self, output_dir: str) -> None:
        self.output_dir = output_dir

    def save_cache(self):
        if get_config().get("persist_cache_as_db", False):
            os.makedirs(self.output_dir, exist_ok=True)
            file_path = os.path.join(self.output_dir, self.filename)
            with open(file_path, 'w') as f:
                json.dump(self.namespaces, f)

    def load_cache(self):
        if get_config().get("persist_cache_as_db", False):
            file_path = os.path.join(self.output_dir, self.filename)
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    self.namespaces = json.load(f)

    def add_document(self, namespace: str, collection_name: str, document_id: str, data: Dict[str, Any]) -> None:
        self.namespaces.setdefault(namespace, {}).setdefault(collection_name, {})[document_id] = data
        self.save_cache()

    def get_document(self, namespace: str, collection_name: str, document_id: str) -> Optional[Dict[str, Any]]:
        return self.namespaces.get(namespace, {}).get(collection_name, {}).get(document_id)

    def update_document(self, namespace: str, collection_name: str, document_id: str, data: Dict[str, Any]) -> None:
        if namespace in self.namespaces and collection_name in self.namespaces[namespace] and document_id in self.namespaces[namespace][collection_name]:
            self.namespaces[namespace][collection_name][document_id].update(data)
            self.save_cache()

    def delete_document(self, namespace: str, collection_name: str, document_id: str) -> None:
        if namespace in self.namespaces and collection_name in self.namespaces[namespace] and document_id in self.namespaces[namespace][collection_name]:
            del self.namespaces[namespace][collection_name][document_id]
            self.save_cache()

    def list_collection(self, namespace: str, collection_name: str) -> List[Dict[str, Any]]:
        return list(self.namespaces.get(namespace, {}).get(collection_name, {}).values())

    def query_collection(self, namespace: str, collection_name: str, query_params: Optional[Dict[str, Any]] = None) -> List[Dict]:
        all_docs = self.list_collection(namespace, collection_name)
        if not query_params:
            return all_docs

        filtered_docs = [doc for doc in all_docs if all(doc.get(key) == value for key, value in query_params.items())]
        return filtered_docs

    def clear_namespace_data(self, namespace: str) -> None:
        if namespace in self.namespaces:
            self.namespaces[namespace].clear()
            self.save_cache()

    def clear_all_data(self) -> None:
        self.namespaces.clear()
        self.save_cache()

# Usage example
cache_handler = CacheHandler()

