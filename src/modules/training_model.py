from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, recall_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score, accuracy_score, precision_score



def training_model(df_final):
    try:        
        X = df_final.drop('NObeyesdad', axis=1)
        y = df_final['NObeyesdad']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        DecisionTreeClassifier().fit(X_train, y_train)
        predictions = DecisionTreeClassifier().predict(X_test)
        recall = recall_score(y_test, predictions, average='weighted')
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions, average='weighted', zero_division=1)

        print(f"Model: {model_name}")
        print(f"Recall: {recall}")
        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print("-" * 50)
    except Exception as e:
        print(f"Error occurred while cleaning the data: {str(e)}")
        return None, None
