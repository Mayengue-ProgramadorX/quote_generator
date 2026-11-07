# Title – # **Quote_Generator**

This program that randomly selects and displays a quote from a collection of famous authors. The program uses Python's built-in random module and the **random.choices() function.**


**Features**
### **1. Quote Collection
The program stores quotes as tuples inside a list:
   **("The only thing we have to fear is fear itself.", "Franklin D. Roosevelt")**
    Each tuple contains:
      - Quote text
      - Author name


### **2. Random Quote Selection
A random quote is selected using:
   **books = random.choices(data_quotes)**

The **random.choices()** function returns a list containing one randomly selected quote from the collection.


### **3. Quote and Author Extraction
The program loops through the selected result and unpacks each tuple:
   **for quote, author in books:**
     This separates:
        quote → quotation text
        author → author's name

### **4. Formatted Output
The quote is displayed using an f-string:
    **print(f'"{quote}" — {author}')**
     "Life is what happens when you're busy making other plans." — John Lennon    

### **How to Run
**python main.py**


### **Example Output
================== QUOTES==============

"The only true wisdom is in knowing you know nothing." — Socrates
