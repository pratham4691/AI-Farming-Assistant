import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

# Define image dimensions
IMG_HEIGHT, IMG_WIDTH = 128, 128

# Data preparation
train_data_gen = ImageDataGenerator(rescale=1./255, 
                                    rotation_range=20, 
                                    width_shift_range=0.2,
                                    height_shift_range=0.2, 
                                    zoom_range=0.2,
                                    horizontal_flip=True)

train_data = train_data_gen.flow_from_directory(
    'dataset/train',
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=32,
    class_mode='categorical'
)

val_data_gen = ImageDataGenerator(rescale=1./255)
val_data = val_data_gen.flow_from_directory(
    'dataset/val',
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=32,
    class_mode='categorical'
)

# Model architecture
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(train_data.num_classes, activation='softmax')
])

model.compile(optimizer=Adam(learning_rate=0.001), 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Training the model
model.fit(
    train_data,
    validation_data=val_data,
    epochs=20,
    steps_per_epoch=train_data.samples // 32,
    validation_steps=val_data.samples // 32
)

# Save the trained model
model.save('plant_disease_model.tflite')