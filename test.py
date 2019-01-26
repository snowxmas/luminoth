import pickle

from luminoth import predict

def __main():
    # requested packeges:
    # dm-sonnet, easydict, scikit-video, click
    with open( "param.pickle", "rb" ) as file:
        param = pickle.load( file )

    predict.do_predict( **param )

if __name__ == "__main__":
    __main()
