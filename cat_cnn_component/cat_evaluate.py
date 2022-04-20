import tensorflow as tf
import tensorflow_addons as tfa

def model_evaluate(model, label_names):
    AUTOTUNE = tf.data.experimental.AUTOTUNE
    
    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "../cat-breed-vol-1/dataset/dataset/images/",
    validation_split=0.2,
    subset="validation",
    seed=111,
    image_size=(200, 200),
    batch_size=10,
    label_mode='categorical',
    class_names=label_names)
    
    model.compile(optimizer = tf.keras.optimizers.Adam(),
             loss=tf.losses.CategoricalCrossentropy(),
             metrics=["accuracy", "AUC", tfa.metrics.F1Score(len(label_names))])
    
    val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)
    result = model.evaluate(val_ds, verbose=2)
    accurancy = result[1]
        
    return result