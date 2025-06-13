# 🩺 Cloud-Based Healthcare Analytics Dashboard

## ✨ Overview

This project simulates a cloud data analytics pipeline focused on synthetic healthcare data. It demonstrates secure cloud storage with AWS S3, Python-based ETL processing, and an interactive dashboard built with Streamlit. Ideal for showcasing real-world skills in cloud integration, data processing, and visualization.

## 🧰 Tech Stack

- **AWS S3** – Secure cloud object storage for patient records
- **Python (pandas, boto3)** – Data generation, transformation, and retrieval
- **Streamlit** – Interactive data dashboard
- **dotenv** – Securely manage environment variables
- **Docker** – For containerized deployment (coming soon)

---

## 🚀 Features

- Generate synthetic healthcare datasets (age, BMI, chronic conditions)
- Upload and retrieve files using AWS S3
- Analyze data and compute key health insights
- Visualize trends using Streamlit (e.g. condition and age distributions)
- Secure handling of credentials using a `.env` file

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Wonder3r/Cloud-Engineer---Project.git
cd Cloud-Engineer--Project
```

### 2. Install dependencies

Use the included `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory (next to your Python scripts) and add your AWS credentials:

```env
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=your-region
S3_BUCKET_NAME=your-bucket-name
```

⚠️ **Do not share your `.env` file or push it to GitHub**  
Make sure your `.gitignore` file includes this line:

```
.env
```

---

## 🔄 Workflow

### ✅ 1. Generate patient data

```bash
python patient_data_generator.py
```

This creates `patients.csv` with 1,000 synthetic patient records.

### ☁️ 2. Upload file to AWS S3

You can manually upload `patients.csv` to your S3 bucket via the AWS Console.

### 🔍 3. Process and analyze data

```bash
python process_data.py
```

This script reads the data from S3, computes the average age, and prints condition distributions.

### 📊 4. Launch the dashboard

```bash
streamlit run dashboard.py
```

This opens a web dashboard in your browser where you can visually explore chronic condition patterns and age trends.

---

## 📸 Dashboard Preview

![Main dashboard view](assets/HealthcareDashboard-top.png)
![Age Distribution](assets/HealthcareDashboard-bottom.png)


---

## 🔮 Future Enhancements

- Docker support for easier deployment

---

## 💼 About Me

Created by Yareth Acosta
Open to roles in cloud engineering and data analytics. Lets Connect! 

