import re

# Regular expression for detecting C# class signatures
class_signature_pattern = r'''
    ^                             # Start of the line
    (public|private|protected|internal|None)?\s*  # Optional access modifier
    class\s+                     # The class keyword followed by space(s)
    ([A-Za-z0-9]\w*)                   # Class name (assuming it starts with an uppercase letter)
    \s*(?::\s*([A-Z]\w*|[\s,<>]+))?\s*  # Optional base class and interfaces
    \{?                          # Optional opening brace (not part of signature)
    '''

# Regular expression for detecting C# method signatures
method_signature_pattern = r'''
    ^                             # Start of the line
    (?!static)                   # Exclude static methods (optional)
    (public|private|protected|internal|)?\s*   # Optional access modifier
    (void|[A-Za-z0-9<>,\s]+)      # Return type (can include generic types)
    \s+                          # Space(s) before the method name
    (\w+)                        # Method name (assuming it follows C# conventions)
    \s*\(                        # Opening parenthesis for parameters
    ([\w\s,<>?]+)?              # Parameters (optional: types followed by names)
    \)\s*                       # Closing parenthesis and optional spaces
    (:\s*\w+)?                   # Optional return type constraint (e.g., `: T`)
    \{?                          # Optional opening brace (start of method body)
    '''

# Example C# code for testing
csharp_code = '''
public class MyClass {
    private int Add(int a, int b) {
        return a + b;
    }

    public void Display() {
        Console.WriteLine("Hello World");
    }
}

internal class anotherClass : BaseClass {
    public void DoSomething() { }
}

protected class YetAnotherClass { }

public class GenericClass<T> {
    public T GetValue() { return default(T); }
}
'''

# Function to extract class and method signatures
def extract_signatures(code):
    class_signatures = re.findall(class_signature_pattern, code, re.VERBOSE | re.MULTILINE)
    method_signatures = re.findall(method_signature_pattern, code, re.VERBOSE | re.MULTILINE)
    print(class_signatures)
    print(method_signatures)
    # Process found signatures for readability
    class_results = [' '.join(filter(None, sig)) for sig in class_signatures]
    method_results = [' '.join(filter(None, sig)) for sig in method_signatures]
    
    return class_results, method_results

# Extract signatures from the example C# code
classes, methods = extract_signatures(csharp_code)

# Output the extracted class and method signatures
print("Extracted Class Signatures:")
print(type(classes))

for cls in classes:
    print(cls)
    print(cls.split(' ')[1])
    

print("\nExtracted Method Signatures:")
for method in methods:
    print(method)
