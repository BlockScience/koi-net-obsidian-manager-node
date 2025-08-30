from rid_lib.core import ORN


class ObsidianVault(ORN):
    namespace = "obsidian.vault"
    
    def __init__(self, vault_id: str):
        self.vault_id = vault_id
        
    @property
    def reference(self):
        return self.vault_id
    
    @classmethod
    def from_reference(cls, reference):
        return cls(reference)
    

class ObsidianNote(ORN):
    namespace = "obsidian.note"
    
    def __init__(self, vault_id: str, note_id: str):
        self.vault_id = vault_id
        self.note_id = note_id
        
    @property
    def reference(self):
        return f"{self.vault_id}/{self.note_id}"
    
    @classmethod
    def from_reference(cls, reference):
        components = reference.split("/")
        if len(components) == 2:
            return cls(*components)
        else:
            raise ValueError("Obsidian note reference must contain two '/'-separated components: <vault_id>/<note_id>")