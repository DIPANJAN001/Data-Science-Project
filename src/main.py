from data.data_loader import load_data
#from data.data_preprocessing import data_preprocess
from data.config import filepath
from data.data_splitting import data_spliting
from data.data_vizualization import plot
def main():
    # Load data
    data = load_data(filepath)
    x,y=data_spliting(data)

   

    

if __name__=="__main__":
    main()