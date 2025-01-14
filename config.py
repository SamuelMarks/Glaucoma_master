import os

MY_SLACK_TOKEN = ''

PROJECT = "D:\\Projects\\my_Glaucoma_project"
IMAGE_LOC = os.path.join(PROJECT,"dataset\\Glaucoma")
TRAIN_IMAGE = os.path.join(IMAGE_LOC,'Training400')
TEST_IMAGE = os.path.join(IMAGE_LOC,'Test')

TRAIN_FILE = os.path.join(IMAGE_LOC,'train.tfrecord')
TEST_FILE = os.path.join(IMAGE_LOC,'test.tfrecord')

RESULT_PATH = os.path.join(PROJECT, "result")
# 
LABEL = {'Glaucoma': 1,
 'Non-Glaucoma': 0}

# Image shape to resahpe the image
# h,w, chennel
IMAGE_SHAPE = (299, 299, 3) # orignal size -(2056, 2124, 3)
COPY_IMAGE = 1

SEND_MESSAGE = False
SAVE_CHECKPOINT = True
EARLY_STOPPING = True


# training options
class TrainOption():
    def __init__(self):
        self.LEARNING_RATE = 1e-5
        self.LR_DEACY_STEPS = 2000
        self.LR_DECAY_RATE = 0.96
        self.MOMENTUM = 0.9
        self.WEIGHT_DECAY = 0.0001
        self.BATCH_SIZE = 1
        self.EPOCHS = 100
        self.STEP_PER_EPOCH = None #1562
        self.DROPOUT_RATE = 0.0
        
