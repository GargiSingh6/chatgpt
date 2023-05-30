import numpy as np
class VectorDatabase:
    def __init__(self):
        self.vectors = {}
    def add_vector(self, key, vector):
        if key in self.vectors:
            print(f"Vector with key '{key}' already exists. Use update_vector() to modify it.")
        else:
            self.vectors[key] = vector
    
    def update_vector(self, key, vector):
        if key in self.vectors:
            self.vectors[key] = vector
        else:
            print(f"No vector found with key '{key}'. Use add_vector() to create a new vector.")
    
    def delete_vector(self, key):
        if key in self.vectors:
            del self.vectors[key]
            print(f"Vector with key '{key}' deleted successfully.")
        else:
            print(f"No vector found with key '{key}'.")
    
    def get_vector(self, key):
        if key in self.vectors:
            return self.vectors[key]
        else:
            print(f"No vector found with key '{key}'.")
    
    def get_all_vectors(self):
        return self.vectors
db = VectorDatabase()
vector1 = np.array([1, 2, 3])
db.add_vector("vector1", vector1)
vector2 = np.array([4, 5, 6])
db.add_vector("vector2", vector2)
updated_vector = np.array([7, 8, 9])
db.update_vector("vector2", updated_vector)
retrieved_vector = db.get_vector("vector1")
print(f"Retrieved vector: {retrieved_vector}")
db.delete_vector("vector2")
all_vectors = db.get_all_vectors()
print(f"All vectors: {all_vectors}")
