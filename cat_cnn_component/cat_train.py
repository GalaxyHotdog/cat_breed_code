import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D


def model_train(input, LR):
    label_names = input
    
    AUTOTUNE = tf.data.experimental.AUTOTUNE
    
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "/home/jovyan/cat-breed-vol-1/dataset/dataset/images/",
    validation_split=0.2,
    subset="training",
    seed=111,
    image_size=(200, 200),
    batch_size=24,
    label_mode='categorical',
    class_names=label_names)
    
    train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
    train_ds = train_ds.repeat()
    
    i_model = InceptionV3(weights= 'imagenet', include_top=False, input_shape=(200, 200, 3))
    for layer in i_model.layers:
        layer.trainable = False
    
    model = Sequential()
    model.add(tf.keras.layers.experimental.preprocessing.Rescaling(1./255))
    model.add(i_model)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(128))
    model.add(Dropout(0.2))
    model.add(Dense(len(label_names), activation = 'softmax'))
    model.build(input_shape=(None, 200, 200, 3))
    
    model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=float(LR)),
             loss=tf.losses.CategoricalCrossentropy(),
             metrics=["accuracy"])
    
    history = model.fit(train_ds, epochs=5, steps_per_epoch=150, verbose=2)
    
    return model