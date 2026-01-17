# LangChain-Structured-OutPut (🦜🔗)

## 1. TypedDict : 
is a way to define a dict in python where specific keys and values should exists. It ensures that your dictionary follows a specific structure.
### When to use ✅ : 
- You're working with dictionaries inside your own Python code
- You want your editor to give you autocomplete hints
- The data is simple and you control where it comes from
- You're working with existing code that uses dictionaries and you want to add type hints without changing everything

## 2. Pydantic :
Pydantic is a data validation and data parsing library for python. It ensures that the data you work with is correct, structured and type-safe.
### When to use ✅ :
- You're receiving data from external sources (APIs, users, LLMs)
- You need validation (age must be positive, email must be valid format, CGPA between zero and ten)
- You need automatic type conversion
- You're building APIs or working with complex data models
- You want clear error messages when data is wrong

## Json :
is just raw data , it's like writing information on a piece of paper. There's no enforcement, no validation, just pure data storage and transmission.
### When to use ✅ :
- You're just storing or transmitting data between systems
- You're reading from or writing to files
- You're sending data over HTTP APIs
- You don't need any Python-specific features
