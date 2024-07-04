# Car Sales Advertisement Dashboard

This project presents a comprehensive web application dashboard built with Streamlit. The application performs exploratory data analysis on a dataset of car sales advertisements, providing valuable insights through interactive visualizations.

## Features

- **Data Viewer**: Display the dataset with the option to include or exclude manufacturers with less than 1000 ads.
- **Vehicle Types Analysis**: Visualize the distribution of vehicle types by manufacturer.
- **Condition vs. Model Year**: Explore the relationship between vehicle condition and model year.
- **Price Distribution Comparison**: Compare price distributions between different manufacturers.

## Setup and Installation

Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Harewavy/EDA_2.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd EDA_2
    ```

3. **Create and Activate a Python Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Exploratory Data Analysis

The exploratory data analysis (EDA) notebook contains the initial analysis and visualizations. You can find the notebook in the `notebooks` directory. To run the notebook:

1. **Navigate to the Notebooks Directory**:
    ```bash
    cd notebooks
    ```

2. **Start Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```

Open `EDA.ipynb` in Jupyter to explore the data analysis.

## Live Demo

You can access the live application here:
[Car Sales Advertisement Dashboard](https://<APP_NAME>.onrender.com)

(*Replace `<APP_NAME>` with your actual Render app name*)

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more details.

---

Thank you for checking out our project! We hope you find it useful and informative.
