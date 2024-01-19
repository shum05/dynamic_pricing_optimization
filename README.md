
# Dynamic Pricing Optimization

This project implements a dynamic pricing optimization model using game theory principles. It allows businesses to determine optimal pricing strategies based on historical data, demand factors, seasonal influences, and competitor pricing.

## Getting Started

Follow these steps to run the project locally:

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/dynamic_pricing_optimization.git
    ```

2. Navigate to the project directory:

    ```bash
    cd dynamic_pricing_optimization
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Flask application:

    ```bash
    python run.py
    ```

2. Open your browser and go to [http://localhost:5000/](http://localhost:5000/)

3. Fill in the form with the required parameters:
   - Historical Price
   - Demand Factor
   - Seasonal Factor
   - Competitor Price

4. Click the "Run Model" button.

5. View the optimal pricing results on the results page.

## Project Structure

- **app/**: Contains the Flask application code.
- **data/**: Placeholder directory for input data.
- **notebooks/**: Jupyter notebooks for various stages of the project.
- **venv/**: Virtual environment directory.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **config.py**: Configuration file for Flask.
- **README.md**: Project documentation.
- **requirements.txt**: List of Python dependencies.
- **run.py**: Script to run the Flask application.

