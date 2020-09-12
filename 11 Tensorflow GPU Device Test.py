# Tensorflow version < 2.0

import sys
import tensorflow as tf

from tensorflow import keras

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

print(f'Python version : {sys.version}')
print(f'Tensorflow version : {tf.__version__}{"-gpu" if tf.config.experimental.list_physical_devices("GPU") else ""}')
print(f'Keras version : {keras.__version__}')

print(f'\n사용 가능한 GPU Device: {tf.test.gpu_device_name()}')
    
      
      
      
# Tensorflow version >= 2.0

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import sys
import tensorflow as tf

from tensorflow import keras

print(f'Python version : {sys.version}')
print(f'Tensorflow version : {tf.__version__}{"-gpu" if tf.config.list_physical_devices("GPU") else ""}')
print(f'Keras version : {keras.__version__}')

print(f'\n사용 가능한 GPU Device: {tf.test.gpu_device_name()}')
