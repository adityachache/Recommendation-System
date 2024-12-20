# **Product Recommendation System**

## **📘 Project Overview**
The **Product Recommendation System** is a web application that demonstrates how recommendation systems can be built using **association rules** and **clustering techniques**. It allows users to explore product clusters, visualize product data, and receive product recommendations based on the **Apriori algorithm** for association rules.

The system identifies relationships between products that are frequently bought together and groups similar products into clusters. This approach is widely used in **e-commerce**, **retail**, and **online shopping platforms** to suggest items to users, thereby enhancing customer experience and driving sales.

### **🌐 WebApp Demo**
**Check out the live demo here:** [Product Recommendation System](https://recommendation-system-uzjhr7bjkxfpszneb3vya2.streamlit.app/)

---

## **📋 Key Features**

### 🔍 **1. Product Recommendations**
- Uses the **Apriori algorithm** to suggest products that are frequently bought together.
- Recommendations are displayed in a simple, easy-to-read format.
- Users can enter a product name and see the associated products based on the filtered association rules.

### 📊 **2. Product Clusters and Visualizations**
- Clusters products into groups based on shared characteristics.
- Displays visual insights using **Plotly interactive charts**, including:
  - **Total Products Sold Per Month**
  - **Top 10 Brands by Product Count**
  - **Top 10 Product Categories by Product Count**
  - **Top 10 Most Expensive and Cheapest Products**
  - **Price Distribution Histogram**

### 📈 **3. Interactive Dashboard**
- Users can interact with the dashboard via **filters** to view products by **price range**, **brand**, and **category**.
- Key performance indicators (KPIs) display total products, unique brands, and total clusters.

### 💡 **4. Dynamic Data Handling**
- Data is loaded dynamically from **Google Drive** using **gdown** to bypass Google Drive's file size limits.
- The system handles large datasets efficiently, even for large CSV files.

---

## **🛠️ Tech Stack**
| **Technology**         | **Usage**                           |
|-----------------------|-------------------------------------|
| **Python**             | Core programming language          |
| **Streamlit**          | Web app framework for UI/UX        |
| **Pandas**             | Data manipulation and analysis     |
| **Plotly**             | Interactive data visualizations    |
| **Apriori Algorithm**  | Association rules for recommendations |
| **gdown**              | To download CSV files from Google Drive |

---

## **📂 Project Structure**
```
📦 recommendation-system
 ┣ 📂 data
 ┃ ┗ 📜 clusters.csv  # Data file containing product information (stored on Google Drive)
 ┣ 📂 pages
 ┃ ┗ 📜 Visualizations.py  # Page containing all visualizations and analytics
 ┣ 📜 app.py  # Main file to run the Streamlit app
 ┣ 📜 README.md  # Project summary and instructions
 ┗ 📜 requirements.txt  # List of dependencies and libraries
```
---

## **⚙️ How to Run the Project Locally**
Follow these instructions to run the **Product Recommendation System** on your local machine.

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your_username/recommendation-system.git
cd recommendation-system
```

### 2️⃣ **Install Required Packages**
Ensure you have Python installed. Then, run:
```bash
pip install -r requirements.txt
```
This will install **Streamlit**, **Pandas**, **Plotly**, **gdown**, and other required libraries.

### 3️⃣ **Run the Streamlit App**
```bash
streamlit run app.py
```
This will launch the app on **http://localhost:8501** in your web browser.

---

## **📁 Data Description**
The file `clusters.csv` contains the following columns:
- **order_id**: Unique identifier for the order
- **product_id**: Unique identifier for the product
- **category_code**: Product category (e.g., electronics, fashion, etc.)
- **brand**: Product brand
- **price**: Price of the product
- **month, day, year**: Date of purchase
- **Cluster**: Cluster ID to which the product belongs
- **item**: Concatenation of category and brand (used for association rules)

The data is loaded directly from **Google Drive** to avoid file size issues.

---

## **📈 Visualizations in the Dashboard**
| **Visualization**                   | **Description**                                        |
|-------------------------------------|------------------------------------------------------|
| **Total Products Sold Per Month**   | Shows monthly product sales count                    |
| **Top 10 Brands**                   | Displays brands with the most products               |
| **Top 10 Product Categories**       | Displays categories with the most products           |
| **Top 10 Most Expensive Products**  | Table of the top 10 most expensive products          |
| **Top 10 Cheapest Products**        | Table of the top 10 cheapest products                |
| **Price Distribution (Histogram)**  | Shows the distribution of product prices            |

All visualizations are built using **Plotly** for interactivity.

---

## **📘 How Recommendations Work**
1. **Association Rules**: Uses the **Apriori algorithm** to discover relationships between products frequently bought together.
2. **Antecedents and Consequents**: If **product A** is bought, the system will recommend **product B** (frequent patterns).
3. **User Input**: Users input the name of a product, and the system displays associated product recommendations.

---

## **🔍 Example User Journey**
1. **Enter Product**: The user enters "electronics.smartphone_apple".
2. **View Recommendations**: The system shows products frequently bought with the iPhone.
3. **Explore Clusters**: Users can select clusters to view similar products.
4. **View KPIs**: The dashboard shows the total products, unique brands, and total clusters.

---

## **🛠️ Future Enhancements**
- **Authentication**: Allow users to sign in to get personalized recommendations.
- **More Visualizations**: Add a timeline of product prices, popularity trends, and more.
- **Improved Filtering**: Advanced filtering options like brand, category, and price sliders.
- **Download Options**: Enable users to download product data.

---

## **🤝 Contributing**
Contributions are welcome! Here’s how you can get involved:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request.

---

## **📜 License**
This project is licensed under the **MIT License**. See the `LICENSE` file for more information.

---

## **📞 Contact**
For any questions or feedback, feel free to contact:
- **Email**: [your_email@example.com](mailto:your_email@example.com)
- **GitHub**: [Your GitHub Profile](https://github.com/your_username/)

If you found this useful, give it a ⭐ on GitHub!

---

**🚀 Check out the live demo here:** [Product Recommendation System](https://recommendation-system-uzjhr7bjkxfpszneb3vya2.streamlit.app/)

