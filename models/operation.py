class Operation:
    def __init__(self, operation: str, result: int):
        self.operation = operation  # The operation as a string, e.g., "2+2"
        self.result = result        # The result of the operation as an integer

    def __repr__(self):
        return f"Operation({self.operation}, {self.result})"
    
    def to_dict(self):
        return {
            "operation": self.operation,
            "result": self.result
        }
