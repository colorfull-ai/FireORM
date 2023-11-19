import os
import firebase_admin
from firebase_admin import credentials

class FirebaseLibraryConfig:
    def __init__(self, read_write_to_cache: bool = False, firebase_credentials_path: str = None):
        self.read_write_to_cache = read_write_to_cache
        # Set default credentials path if not provided
        self.firebase_credentials_path = firebase_credentials_path or os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "firebase_sa.json"
        )

# Global configuration instance
global_config = FirebaseLibraryConfig()

def set_library_config(**kwargs):
    global global_config
    for key, value in kwargs.items():
        if hasattr(global_config, key):
            setattr(global_config, key, value)

def initialize_firebase():
    try:
        # Check if Firebase app is already initialized
        firebase_admin.get_app()
    except ValueError:
        # First check for the standard environment variable
        cred_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', None)
        
        # If not found, use the path from the configuration
        if not cred_path:
            cred_path = global_config.firebase_credentials_path

        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)

# # Example usage by library users
# from your_library import set_library_config

# # Set custom Firebase credentials path and test mode
# set_library_config(
#     firebase_credentials_path="/path/to/custom/firebase_sa.json",
#     test_mode=True
# )

# # Initialize Firebase with custom configurations
# initialize_firebase()
