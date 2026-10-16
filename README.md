# Stock Market Prediction & Analytics Dashboard

A complete, end-to-end Machine Learning pipeline and interactive analytical dashboard covering three problem tracks: **Regression**, **Classification**, and **Clustering**. The repository contains full data preprocessing, exploratory data analysis (EDA), model training, hyperparameter tuning, benchmark comparison, and an interactive web GUI.

---

## Repository Structure

```text
Stock-Market-Prediction/
├── app/                              # Web GUI deployment folder (Rubric Bonus Requirement)
│   ├── app.py                        # Streamlit application entrypoint
│   ├── ui_styles.py                  # Bespoke organic design system (zero emojis)
│   └── utils.py                      # Sub-millisecond cached inference pipelines
├── data/                             # Raw & processed financial datasets
│   ├── djia4_regression_data.csv     # Dow Jones 4-constituent OHLCV historical prices
│   └── stock_data.csv                # Technical momentum indicators & sentiment
├── models/                           # Serialized pre-trained scikit-learn model bundles
│   ├── regression_bundle.joblib      # 10 regression models + ColumnTransformer
│   ├── classification_bundle.joblib  # 10 classification models + SMOTE + Scaler
│   ├── clustering_bundle.joblib      # KMeans (k=4) + PCA + cluster centroids
│   └── benchmark_metrics.json        # Comprehensive evaluation metrics across tracks
├── Notebook/                         # Jupyter Notebook deliverables (Tracks 1, 2, & 3)
│   ├── Regression.ipynb              # Track 1: Stock price log-return forecasting
│   ├── Classification.ipynb          # Track 2: Trade signal classification (Part A & B)
│   └── Clustering.ipynb              # Track 3: Market regime segmentation
├── .streamlit/
│   └── config.toml                   # Theme configuration (Warm Ivory & Sage)
├── requirements.txt                  # Pinned production Python dependencies
├── run_app.bat                       # 1-Click Windows launch script
└── README.md                         # Documentation & Rubrics mapping
```

---

## Machine Learning Problem Tracks

### Track 1: Stock Return Regression
- **Target**: Next-day log return of DJIA constituent equities (`AAPL`, `BA`, `JPM`, `KO`).
- **Feature Engineering**: Stationary log return ratios, intraday high-low volatility, open-close delta, lag returns ($t-1, t-2$), 5-day rolling standard deviation, and volume percentage change.
- **Models Benchmarked**: 10 architectures (Linear Regression, Ridge, Lasso, ElasticNet, Polynomial Ridge Degree 2, SVR, KNN, Decision Tree, Random Forest, Gradient Boosting).

### Track 2: Trade Signal Classification (Review 2 Part A & Part B)
- **Target**: Institutional Buy signal (`1`) vs Hold/Exit (`0`).
- **Part A (Classical Supervised)**: Logistic Regression, K-Nearest Neighbors, Gaussian Naive Bayes, Decision Tree, Support Vector Classifier (SVC).
- **Part B (Ensemble & Advanced)**: Random Forest, AdaBoost, Gradient Boosting, Bagging Classifier, MLP Neural Network.
- **Class Balancing**: SMOTE resampling + Decision threshold tuning.

### Track 3: Market Regime Clustering (Review 2 Part C)
- **Target**: Macroeconomic & volatility market regime segmentation.
- **Methodology**: StandardScaler normalization, K-Means ($k=4$), Agglomerative Hierarchical clustering, and 2D Principal Component Analysis (PCA) projection.

---

## Running the Web GUI (`/app`)
LINK : https://stock-market-prediction-xh9zzt82ysrvn8xmp2d2vw.streamlit.app/
