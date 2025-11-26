import pickle

model_path = os.path.join(results_folder, "soh_model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(model, f)
