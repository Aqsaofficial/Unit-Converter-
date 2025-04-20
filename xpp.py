 

---

## 🌐 Project Overview

This project involves creating a web-based unit converter that allows users to convert between various units such as length, temperature, and weight. The application will be built using Python and Streamlit, providing a simple and interactive user interface.

---

## 🛠️ Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Visual Studio Code (VS Code)**: [Download VS Code](https://code.visualstudio.com/)
- **Streamlit Library**: Install via pip

  ```bash
  pip install streamlit
  ```

---

## 🧱 Step-by-Step Guide

### 1. **Set Up Your Project Directory**

Create a new directory for your project and navigate into it:

```bash
mkdir unit_converter_app
cd unit_converter_app
```

### 2. **Create the Application Script**

In your project directory, create a file named `app.py` and open it in VS Code. Add the following code:

```python
import streamlit as st

# Title of the app
st.title("Unit Converter")

# Sidebar for user input
st.sidebar.header("Select Conversion Type")

# Conversion options
conversion_type = st.sidebar.selectbox(
    "Choose the type of conversion:",
    ["Length", "Temperature", "Weight"]
)

# Conversion logic
if conversion_type == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters"]
    conversion_map = {
        ("Meters", "Kilometers"): 0.001,
        ("Kilometers", "Meters"): 1000,
        ("Centimeters", "Meters"): 0.01,
        ("Millimeters", "Meters"): 0.001,
    }
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    conversion_map = {
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
    }
else:  # Weight
    units = ["Kilograms", "Grams", "Pounds"]
    conversion_map = {
        ("Kilograms", "Grams"): 1000,
        ("Grams", "Kilograms"): 0.001,
        ("Kilograms", "Pounds"): 2.20462,
        ("Pounds", "Kilograms"): 0.453592,
    }

# User input fields
value = st.number_input(f"Enter value in {units[0]}:", min_value=0.0, format="%.2f")
from_unit = st.selectbox(f"Convert from {conversion_type}:", units)
to_unit = st.selectbox(f"Convert to {conversion_type}:", units)

# Conversion function
def convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if conversion_type == "Temperature":
        return conversion_map[(from_unit, to_unit)](value)
    return value * conversion_map.get((from_unit, to_unit), 1)

# Perform conversion and display result
if st.button("Convert"):
    result = convert(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")
```

### 3. **Run the Application**

In the terminal, navigate to your project directory and run:

```bash
streamlit run app.py
```

This command will start the Streamlit server and open the application in your default web browser.

---

## 📦 Optional: Share Your Application

To share your application with others, you can deploy it using services like:

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Heroku](https://www.heroku.com/)

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Panaversity Learn Modern AI Python Repository](https://github.com/panaversity/learn-modern-ai-python)

---

