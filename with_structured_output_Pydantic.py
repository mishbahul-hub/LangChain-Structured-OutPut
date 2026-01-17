from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen3-32B",
    task = "text-generation",
    provider = "together"
)

model = ChatHuggingFace( llm = llm )

# schema for structured output

class review(BaseModel):
    
    KeyThemes : list[str] = Field(description = "the main themes discussed in this review")
    summary : str = Field(description = "a brief summary of the product review")
    pros : Optional[list[str]] = Field(description = "the positive aspects of the product")
    cons : Optional[list[str]] = Field(description = "the negative aspects of the product")
    sentiment : Literal["postive", "negative"] = Field("overall sentiment of the review")
    title : Optional[str] = Field("a cachy title for the review")

structured_model = model.with_structured_output( review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

# print("Structured Review Output: ", result)

print(result)