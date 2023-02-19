import os
import numpy as np

# paths

REPO_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EM_DATA_DIR = os.path.join(REPO_DIR, 'data_em')
LM_DATA_DIR = os.path.join(REPO_DIR, 'data_lm')
TEST_DATA_DIR = os.path.join(REPO_DIR, 'data_test')
MODEL_DIR = os.path.join(REPO_DIR, 'models')
RESULT_DIR = os.path.join(REPO_DIR, 'results')

# GPT encoding model parameters

TRIM = 5
STIM_DELAYS = [1, 2, 3, 4]
RESP_DELAYS = [-4, -3, -2, -1]
ALPHAS = np.logspace(1, 3, 10)
NBOOTS = 50
VOXELS = 10000
CHUNKLEN = 40
GPT_LAYER = 9
GPT_WORDS = 5

# decoder parameters

RANKED = True
WIDTH = 200
NM_ALPHA = 2/3
LM_TIME = 8
LM_MASS = 0.9
LM_RATIO = 0.1
EXTENSIONS = 5

# devices

GPT_DEVICE = 'cuda'
EM_DEVICE = 'cuda'
SM_DEVICE = 'cuda'