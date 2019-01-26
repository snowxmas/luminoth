import pickle

from luminoth import predict

def __main():
    with open( "param.pickle", "rb" ) as file:
        param = pickle.load( file )

    predict.do_predict( **param )

if __name__ == "__main__":
    __main()
