import kagglehub
import os

# Download latest version
def download_dataset():
    #define the path for saving:
    project_path = os.path.join(os.getcwd(), "data")
    
    #create the folder if not existing
    os.makedirs(project_path, exist_ok=True)
    
    resolved_path =  kagglehub.dataset_download(
        "vinicius150987/titanic3",
        output_dir=project_path,
        force_download= False
        )
    
    return resolved_path
    

if __name__ == "__main__":
    download_dataset()