from keras.models import load_model

try:
    print("Testing modern model load...")
    model = load_model("stock_sentiment_model.keras")
    print("Model loaded successfully without InternalError!")
except Exception as e:
    print(f"Error loading model: {e}")
